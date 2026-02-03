# Chemical Equipment Parameter Visualizer

## Project Overview

This is a web-based data visualization application that analyzes chemical equipment data from CSV files. Users upload a CSV file containing equipment parameters, and the system automatically calculates statistics and displays visualizations.

## Problem Statement

Process analysts in chemical plants receive CSV files with equipment data and need to:
- Quickly understand equipment status
- Calculate operational averages
- Identify patterns and trends

Manually doing this in Excel is slow and error-prone.

## Solution

This application provides:
- Simple CSV upload interface
- Automatic statistical analysis
- Clear visual representations
- Instant results

## Architecture

### Backend (Django + DRF + Pandas)
- Receives CSV files via REST API
- Processes data using Pandas
- Calculates statistics
- Returns JSON responses
- **Reusable design**: Same APIs can be used by future desktop applications

### Frontend (React + Chart.js)
- Provides upload interface
- Sends files to backend
- Displays results
- Renders charts

### Data Flow
```
User → React → Django → Pandas → Calculations → JSON → React → Display
```

## Features

✅ CSV file upload  
✅ Automatic calculation of:
   - Total equipment count
   - Average flowrate
   - Average pressure
   - Average temperature
   - Equipment distribution by type  
✅ Visual chart display  
✅ Error handling  

## Technology Stack

**Backend:**
- Python 3.10+
- Django 4.x
- Django REST Framework
- Pandas

**Frontend:**
- React 18
- Chart.js
- react-chartjs-2

## Installation

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install django djangorestframework pandas django-cors-headers
python manage.py runserver
```

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

## Usage

1. Open browser to `http://localhost:3000`
2. Click "Choose File" and select a CSV file
3. Click "Analyze Data"
4. View results and charts

## CSV Format

Required columns:
- `equipment_name`
- `equipment_type`
- `flowrate`
- `pressure`
- `temperature`

Example:
```csv
equipment_name,equipment_type,flowrate,pressure,temperature
Pump-A,Pump,120,5.5,310
Reactor-1,Reactor,200,6.2,350
```

## Future Extensibility

The backend is designed to be reusable. The same Django APIs can be consumed by:
- ✅ Web application (current implementation)
- 📋 Desktop application using PyQt5 (planned)
- 📋 Mobile application (potential)

No backend logic needs to be rewritten for desktop implementation.

## Project Structure
```
equipment-visualizer/
├── backend/
│   ├── equipment_backend/
│   │   ├── settings.py
│   │   └── urls.py
│   ├── analyzer/
│   │   ├── views.py
│   │   └── urls.py
│   └── manage.py
└── frontend/
    ├── src/
    │   ├── App.js
    │   ├── App.css
    │   └── index.js
    └── package.json
```

## Testing

Sample CSV file included: `sample_data.csv`

Run both servers and test:
1. Valid CSV upload → Should show statistics and chart
2. No file selected → Should show error message
3. Invalid CSV format → Should show error message

## Author

Developed as a complete full-stack web application demonstrating clean separation of concerns and reusable architecture.
```

---

### **One-Paragraph Project Explanation**

Save this as `PROJECT_SUMMARY.txt`:
```
This project is a web-based data visualization system where a React frontend 
allows users to upload CSV files containing chemical equipment data. The CSV 
is sent to a Django REST API backend that uses Pandas to read the file and 
calculate summary statistics (total equipment count, average flowrate, pressure, 
temperature, and equipment distribution by type). The backend returns these 
results as JSON, which the React frontend displays as both numerical summaries 
and visual charts using Chart.js. The backend is intentionally designed to be 
UI-agnostic and reusable, meaning the same Django APIs can later be consumed 
by a PyQt5 desktop application without any modification to the data processing 
logic. This clean separation of concerns ensures scalability and maintainability.