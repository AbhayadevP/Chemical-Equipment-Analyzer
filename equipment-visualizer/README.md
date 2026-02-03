# Chemical Equipment Parameter Visualizer

A web-based data visualization system where a React frontend uploads CSV files to a Django backend. The backend processes the data using Pandas and exposes summary analytics through APIs. The frontend consumes these APIs to display numbers and charts.

## Project Structure

```
equipment-visualizer/
├── backend/              # Django backend
│   ├── api/             # API app with CSV processing
│   ├── equipment_backend/  # Django project settings
│   ├── manage.py
│   └── requirements.txt
└── frontend/            # React frontend
    ├── src/
    │   ├── components/  # React components
    │   ├── App.js
    │   └── index.js
    └── package.json
```

## Features

- Upload CSV files containing equipment data
- Automatic calculation of:
  - Total number of equipment
  - Average flowrate
  - Average pressure
  - Average temperature
  - Equipment count per type
- Visual charts showing equipment distribution
- Clean separation between frontend and backend

## CSV File Format

The CSV file should contain the following columns (case-insensitive):
- `equipment_name`
- `equipment_type`
- `flowrate`
- `pressure`
- `temperature`

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd equipment-visualizer/backend
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run migrations (if needed):
   ```bash
   python manage.py migrate
   ```

6. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

The backend will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd equipment-visualizer/frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

The frontend will be available at `http://localhost:3000`

## Usage

1. Start both backend and frontend servers (see Setup Instructions above)
2. Open your browser and navigate to `http://localhost:3000`
3. Click "Select CSV File" and choose a CSV file with equipment data
4. View the calculated statistics and charts

## API Endpoint

The backend exposes a single API endpoint:

- **POST** `/api/upload/`
  - Accepts a CSV file via multipart/form-data
  - Returns JSON with calculated statistics

## Technologies Used

- **Backend**: Django 6.0.2, Django REST Framework, Pandas
- **Frontend**: React 18.2.0, Chart.js, Axios
- **CORS**: django-cors-headers for cross-origin requests

## Notes

- The backend is designed to be reusable for future desktop application development
- No authentication or database storage is implemented in this phase
- The system focuses on processing and displaying data, not storing it
