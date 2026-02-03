# Quick Start Guide - Windows PowerShell

## Prerequisites
- Python 3.x installed
- Node.js and npm installed

## Running the Application

You need **TWO terminal windows** - one for backend, one for frontend.

---

## Terminal 1: Backend (Django)

```powershell
# Navigate to backend directory
cd C:\everything\Learn\pr\CEA\equipment-visualizer\backend

# Create virtual environment (if not exists)
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run migrations (if needed)
python manage.py migrate

# Start Django server
python manage.py runserver
```

**Backend will run at:** http://localhost:8000

**Keep this terminal window open!**

---

## Terminal 2: Frontend (React)

Open a **NEW PowerShell window**:

```powershell
# Navigate to frontend directory
cd C:\everything\Learn\pr\CEA\equipment-visualizer\frontend

# Install dependencies (first time only)
npm install

# Start React development server
npm start
```

**Frontend will run at:** http://localhost:3000

The browser should automatically open. If not, manually go to: http://localhost:3000

---

## Using the Application

1. Make sure both servers are running (backend on port 8000, frontend on port 3000)
2. In the browser, click "Select CSV File"
3. Choose the `sample_data.csv` file from the project root
4. View the results and charts!

---

## Troubleshooting

### Backend Issues:
- **Port 8000 already in use?** 
  - Use: `python manage.py runserver 8001` (then update frontend API_URL)
- **Module not found?**
  - Make sure venv is activated: `.\venv\Scripts\Activate.ps1`
  - Reinstall: `pip install -r requirements.txt`

### Frontend Issues:
- **Port 3000 already in use?**
  - React will ask to use a different port, say yes
- **npm install fails?**
  - Make sure Node.js is installed: `node --version`
  - Try: `npm cache clean --force` then `npm install`

### CORS Errors:
- Make sure backend is running on port 8000
- Check that `django-cors-headers` is installed in backend

---

## Stopping the Servers

- **Backend:** Press `Ctrl+C` in the backend terminal
- **Frontend:** Press `Ctrl+C` in the frontend terminal
