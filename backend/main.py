from fastapi import FastAPI, Form, UploadFile, File, WebSocket, WebSocketDisconnect
from pymongo import MongoClient
from datetime import datetime

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from fastapi.middleware.cors import CORSMiddleware


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

client = MongoClient("mongodb://localhost:27017/")
db = client["airdropLAN"]
devices = db["devices"]
files = db["files"]

# Store websocket connections
online_devices = {}   # device_id: websocket


# ------------ real time device tracker ---------------
@app.websocket("/ws")
async def ws_endpoint(ws: WebSocket):
    await ws.accept()

    try:
        data = await ws.receive_json()
        device_id = data["device_id"]
        name = data["name"]

        online_devices[device_id] = {"ws": ws, "name": name}

        # Notify all
        await broadcast_online_devices()

        # Keep connection alive
        while True:
            await ws.receive_text()

    except WebSocketDisconnect:
        # Remove on disconnect
        if device_id in online_devices:
            del online_devices[device_id]
        await broadcast_online_devices()


# Send updated online list
async def broadcast_online_devices():
    payload = {
        "type": "online_devices",
        "devices": [
            {"device_id": d, "name": online_devices[d]["name"]}
            for d in online_devices
        ]
    }

    for d in online_devices.values():
        try:
            await d["ws"].send_json(payload)
        except:
            pass






# ==============================
# EXISTING API ENDPOINTS
# (unchanged)
# ==============================

# registration for new devices 
@app.post("/register")
async def register(device_id: str, name: str):
    devices.update_one(
        {"device_id": device_id},
        {"$set": {"name": name, "last_seen": datetime.utcnow()}},
        upsert=True
    )
    return {"status": "success", "message": "Device registered successfully!"}

# direct route to devices
@app.get("/register_device")
def register_device():
    return FileResponse(os.path.join(FRONTEND_DIR, "register.html"))



# list online devices 
@app.get("/devices")
async def get_devices():
    return list(devices.find({}, {"_id": 0}))



# upload file in devices 
@app.post("/upload")
async def upload(to: str = Form(...), file: UploadFile = File(...)):
    content = await file.read()
    files.insert_one({
        "to": to,
        "file": file.filename,
        "content": content,
        "uploaded_at": datetime.utcnow()
    })
    return {"status": "uploaded"}


# user device receives file 
@app.get("/files/{device_id}")
async def get_files(device_id: str):
    return list(files.find({"to": device_id}, {"_id": 0, "content": 0}))



@app.get("/download/{device_id}/{filename}")
async def download_file(device_id: str, filename: str):
    file_doc = files.find_one({"to": device_id, "file": filename})
    if not file_doc:
        return {"error": "File not found"}

    return Response(
        content=file_doc["content"],
        media_type="application/octet-stream",
        headers={
            "Content-Disposition": f"attachment; filename={filename}"
        }
    )
