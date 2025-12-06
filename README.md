# TransIO 🌐

**TransIO** – Web-based real-time file transfer inspired by Apple AirDrop.  
Send and receive files between devices on the same network quickly and easily.

---

## 🚀 Features

- **Real-Time Device Tracking** – See online devices instantly.  
- **Direct File Transfer** – Send files to other devices without accounts.  
- **Responsive UI** – Clean, minimal, and mobile-friendly.  
- **Dark Mode Support** – Eye-friendly interface.  

---

## 🛠 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-4B0082?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/N0teveryth1ng/transio.git
cd transio
```

### 2. Create Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Create `.env` file in project root:
```
MONGO_URI=mongodb://localhost:27017/
```

For MongoDB Atlas (cloud):
```
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/airdropLAN
```

### 5. Run the Application

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

Access at: **http://localhost:8000/static/register.html**

---

## 🎮 Usage

1. Open the application in your browser
2. Register your device with a name
3. See other online devices in real-time
4. Upload files to any online device
5. Files are instantly available to the recipient

---

## 🛑 Stop the Server

Press `Ctrl + C` in the terminal

---

## 📤 Create a Release

```bash
git tag v1.0.0
git push origin v1.0.0
```

Or with a message:
```bash
git tag -a v1.0.0 -m "First release"
git push origin v1.0.0
```

---

## 📝 License

MIT

---

## 👤 Author

**N0teveryth1ng**
