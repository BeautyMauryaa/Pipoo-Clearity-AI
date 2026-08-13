# Clarity AI Backend

Backend API for Clarity AI - Career clarity, skill proof, and focus platform.

## 🚀 Quick Start

### 1. Create Virtual Environment
```bash
python -m venv venv
```

### 2. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create .env File
Copy `.env.example` to `.env` or create a new `.env` file with required variables.

### 5. Run Server
```bash
uvicorn app.main:app --reload
```

Server will start at: `http://localhost:8000`

## 📚 API Documentation

Once the server is running, access:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## 📁 Project Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── core/
│   │   └── config.py        # Configuration settings
│   ├── routes/              # API endpoints (Step 2)
│   ├── models/              # Database models (Step 3)
│   └── services/            # Business logic (Step 4)
├── .env                     # Environment variables
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## ✅ Health Check

Test if server is running:
```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "service": "Clarity AI Backend",
  "version": "1.0.0"
}
```

## 🔧 Development

### Install New Package
```bash
pip install package-name
pip freeze > requirements.txt
```

### Run with Auto-reload
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 📝 Current Phase: PHASE 2 - BACKEND FOUNDATION

- [x] Step 1: Backend Setup (CURRENT)
- [ ] Step 2: Authentication APIs
- [ ] Step 3: Onboarding APIs
- [ ] Step 4: Workspace Data APIs
- [ ] Step 5: Database Connection
- [ ] Step 6: Frontend-Backend Integration
