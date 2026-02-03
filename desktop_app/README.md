# Chemical Equipment Parameter Visualizer - Desktop Application

A PyQt5 desktop application that analyzes chemical equipment data by uploading CSV files to a Django backend API.

## 🎯 Overview

This desktop application provides a native GUI interface for the Chemical Equipment Parameter Visualizer. It uses the **same Django backend** as the web application, demonstrating backend reusability across different frontend platforms.

### Key Features

✅ Native desktop GUI using PyQt5  
✅ CSV file upload and analysis  
✅ Real-time communication with Django backend  
✅ Visual statistics display  
✅ Interactive bar charts using Matplotlib  
✅ Error handling and user feedback  

---

## 🏗️ Architecture
```
┌─────────────────────────────────────┐
│   Desktop Application (PyQt5)      │
│   - UI Layer (ui_main.py)          │
│   - API Client (api_client.py)     │
│   - Charts (charts.py)             │
└─────────────┬───────────────────────┘
              │
              │ HTTP POST
              │ (CSV file)
              ↓
┌─────────────────────────────────────┐
│   Django Backend (Unchanged)        │
│   - Receives CSV                    │
│   - Processes with Pandas           │
│   - Returns JSON statistics         │
└─────────────────────────────────────┘
```

**Important:** The desktop app does NOT calculate statistics. All processing happens in the Django backend.

---

## 📋 Prerequisites

Before running the desktop application, ensure you have:

1. **Python 3.8 or higher**
```bash
   python --version
```

2. **Django Backend Running**
   - The backend must be running on `http://localhost:8000`
   - See backend setup instructions below

3. **Virtual Environment** (recommended)

---

## 🚀 Installation

### Step 1: Navigate to Desktop App Directory
```bash
cd desktop_app
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv venv_desktop
.\venv_desktop\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
python3 -m venv venv_desktop
source venv_desktop/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

This installs:
- PyQt5 5.15.10 (GUI framework)
- requests 2.31.0 (HTTP client)
- matplotlib 3.8.2 (Charting library)

### Step 4: Verify Installation
```bash
python -c "import PyQt5, matplotlib, requests; print('✓ All packages installed successfully')"
```

---

## ▶️ Running the Application

### Complete Startup Procedure

You need **TWO terminals** - one for backend, one for desktop app.

#### Terminal 1: Start Django Backend
```bash
# Navigate to backend directory
cd ../equipment-visualizer/backend

# Activate backend virtual environment
# Windows:
..\.venv\Scripts\Activate.ps1
# Linux/Mac:
source ../.venv/bin/activate

# Start Django server
python manage.py runserver
```

**Backend will run at:** `http://localhost:8000`

Keep this terminal open!

#### Terminal 2: Start Desktop Application

Open a **NEW terminal**:
```bash
# Navigate to desktop_app directory
cd desktop_app

# Activate desktop virtual environment
# Windows:
.\venv_desktop\Scripts\Activate.ps1
# Linux/Mac:
source venv_desktop/bin/activate

# Run the desktop application
python main.py
```

**Desktop window will open automatically!**

---

## 📖 Usage Guide

### Step-by-Step Usage

1. **Launch Application**
   - Run `python main.py`
   - Main window appears

2. **Upload CSV File**
   - Click "📁 Select CSV File" button
   - Choose a CSV file from your computer
   - File uploads automatically

3. **View Results**
   - Statistics appear in cards:
     - Total Equipment
     - Average Flowrate
     - Average Pressure
     - Average Temperature
   - Bar chart shows equipment distribution

4. **Upload Another File**
   - Simply click "Select CSV File" again
   - Previous results are replaced with new ones

### CSV File Format

Your CSV must have these columns:
```csv
equipment_name,equipment_type,flowrate,pressure,temperature
Pump-A,Pump,120,5.5,310
Reactor-1,Reactor,200,6.2,350
Heater-X,Heater,80,4.1,400
```

**Required Columns:**
- `equipment_name`
- `equipment_type`
- `flowrate`
- `pressure`
- `temperature`

---

## 🧪 Testing

### Test with Sample Data

1. Use the `sample_data.csv` file in the project root:
```bash
# From desktop_app directory
python main.py
# Then select: ../sample_data.csv
```

2. **Expected Results:**
   - Total Equipment: 25
   - Average Flowrate: ~128
   - Average Pressure: ~5.6
   - Average Temperature: ~352
   - Chart shows distribution of Pumps, Reactors, Heaters

### Test Backend Connection

Before launching the app:
```bash
python api_client.py
```

**Expected output:**
```
✓ Backend is running
```

If you see this, backend is ready! ✅

### Test Chart Display
```bash
python charts.py
```

This opens a test window with a sample chart.

---

## 🗂️ Project Structure
```
desktop_app/
├── main.py              # Application entry point
├── ui_main.py           # Main window and UI components
├── api_client.py        # Django backend API communication
├── charts.py            # Matplotlib chart generation
├── requirements.txt     # Python dependencies
├── README.md            # This file
└── venv_desktop/        # Virtual environment (created during setup)
```

---

## 🔧 Troubleshooting

### Problem 1: "Cannot connect to backend server"

**Symptoms:**
- Error dialog appears when selecting CSV
- Status shows "Backend Not Running"

**Solution:**
```bash
# Check if Django is running
# Open browser: http://localhost:8000

# If not running, start it:
cd ../equipment-visualizer/backend
python manage.py runserver
```

---

### Problem 2: "ModuleNotFoundError: No module named 'PyQt5'"

**Symptoms:**
- Error when running `python main.py`

**Solution:**
```bash
# Make sure virtual environment is activated
# Windows:
.\venv_desktop\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

---

### Problem 3: Application window doesn't appear

**Symptoms:**
- Terminal shows no errors
- But window doesn't open

**Solution:**

**On Windows:**
```bash
# Try running with pythonw instead of python
pythonw main.py
```

**On Linux:**
```bash
# Install Qt dependencies
sudo apt-get install python3-pyqt5
```

---

### Problem 4: "Missing columns" error

**Symptoms:**
- CSV uploads but shows error about missing columns

**Solution:**
- Check CSV has exactly these column names (case-sensitive):
  - equipment_name
  - equipment_type
  - flowrate
  - pressure
  - temperature

---

### Problem 5: Chart doesn't display

**Symptoms:**
- Statistics show but chart area is blank

**Solution:**
```bash
# Reinstall matplotlib with Qt backend
pip uninstall matplotlib
pip install matplotlib==3.8.2
```

---

### Problem 6: Port 8000 already in use

**Symptoms:**
- Backend won't start, says port in use

**Solution:**

**Option A - Use different port:**
```bash
# Start backend on port 8001
python manage.py runserver 8001

# Update api_client.py:
# Change: base_url="http://localhost:8000"
# To:     base_url="http://localhost:8001"
```

**Option B - Kill process on port 8000:**

**Windows:**
```bash
netstat -ano | findstr :8000
taskkill /PID <PID_NUMBER> /F
```

**Linux/Mac:**
```bash
lsof -ti:8000 | xargs kill -9
```

---

## 🎨 Features Demonstration

### What the Desktop App Does

1. **File Selection**
   - Native file dialog
   - CSV file filtering
   - Shows selected file name

2. **Background Upload**
   - Non-blocking UI
   - Progress indication
   - Status messages

3. **Results Display**
   - Clean card layout
   - Large, readable numbers
   - Color-coded sections

4. **Interactive Chart**
   - Bar chart with labels
   - Value labels on bars
   - Automatic scaling
   - Color-coded bars

### What the Desktop App Does NOT Do

❌ Read CSV files locally  
❌ Calculate statistics  
❌ Store data  
❌ Modify backend logic  

**All processing happens in Django backend!**

---

## 🔄 Comparison: Web vs Desktop

| Feature | Web App (React) | Desktop App (PyQt5) |
|---------|----------------|---------------------|
| **UI Framework** | React | PyQt5 |
| **File Upload** | HTML input | QFileDialog |
| **HTTP Client** | fetch API | requests library |
| **Charts** | Chart.js | Matplotlib |
| **Backend API** | ✅ Same | ✅ Same |
| **Calculations** | ❌ Backend only | ❌ Backend only |
| **Installation** | npm install | pip install |
| **Running** | npm start | python main.py |

**Both apps use the exact same Django backend API!**

---

## 📝 Technical Details

### API Endpoint Used
```
POST http://localhost:8000/api/analyze/
Content-Type: multipart/form-data

Body:
  file: <CSV file>

Response:
{
  "total_equipment": 25,
  "average_flowrate": 120.0,
  "average_pressure": 5.4,
  "average_temperature": 315,
  "equipment_by_type": {
    "Pump": 10,
    "Reactor": 9,
    "Heater": 6
  }
}
```

### Dependencies Explanation

**PyQt5:**
- Provides native GUI widgets
- Cross-platform (Windows, Mac, Linux)
- Professional look and feel

**requests:**
- HTTP library for Python
- Handles multipart form uploads
- Simple API for POST requests

**matplotlib:**
- Industry-standard charting library
- Integrates with PyQt5
- Highly customizable

---

## 🚦 System Requirements

**Minimum:**
- Python 3.8+
- 4GB RAM
- 100MB disk space
- Windows 10, macOS 10.14, or Ubuntu 18.04

**Recommended:**
- Python 3.10+
- 8GB RAM
- SSD storage
- Modern OS version

---

## 📄 License

This project is part of the Chemical Equipment Parameter Visualizer system.
See main project README for license information.

---

## 🤝 Support

### Getting Help

1. **Check this README** - Most common issues are covered
2. **Check backend README** - Backend setup issues
3. **Test components individually** - Run test commands
4. **Verify installation** - Check all dependencies installed

### Common Questions

**Q: Can I use this without the backend?**  
A: No, the desktop app requires the Django backend to be running.

**Q: Can I modify the backend?**  
A: Yes, but not necessary. The desktop app works with existing backend.

**Q: Can I run multiple instances?**  
A: Yes, each window is independent.

**Q: Can I package this as .exe?**  
A: Yes, using PyInstaller (not covered in this guide).

---

## ✅ Quick Start Checklist

Before first run:

- [ ] Python 3.8+ installed
- [ ] Virtual environment created
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Django backend running (`python manage.py runserver`)
- [ ] Backend accessible at `http://localhost:8000`
- [ ] Sample CSV file ready for testing

Then run:
```bash
python main.py
```

---

## 🎯 Success Criteria

The desktop application is working correctly when:

✅ Window opens without errors  
✅ "Select CSV File" button is clickable  
✅ File dialog opens and lets you select CSV  
✅ Status shows "Processing..." then "✓ Analysis complete!"  
✅ Statistics appear in all four cards  
✅ Bar chart displays with proper labels and colors  
✅ Can upload multiple files in sequence  

---

**Congratulations! You now have a fully functional desktop application that reuses your Django backend!** 🎉