import React, { useState } from 'react';
import './App.css';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';

// Register Chart.js components
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

function App() {
  // State management
  const [selectedFile, setSelectedFile] = useState(null);
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Handle file selection
  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
    setError(null); // Clear any previous errors
  };

  // Handle form submission
  const handleSubmit = async () => {
    // Validation: Check if file is selected
    if (!selectedFile) {
      setError('Please select a CSV file first');
      return;
    }

    // Clear previous results and errors
    setResults(null);
    setError(null);
    setLoading(true);

    // Prepare form data
    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      // Send POST request to Django backend
      const response = await fetch('http://localhost:8000/api/analyze/', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();

      if (response.ok) {
        // Success: Store results
        setResults(data);
      } else {
        // Backend returned an error
        setError(data.error || 'An error occurred while processing the file');
      }
    } catch (err) {
      // Network or other error
      setError('Failed to connect to the server. Make sure the backend is running.');
    } finally {
      setLoading(false);
    }
  };

  // Prepare chart data
  const getChartData = () => {
    if (!results || !results.equipment_by_type) return null;

    const types = Object.keys(results.equipment_by_type);
    const counts = Object.values(results.equipment_by_type);

    return {
      labels: types,
      datasets: [
        {
          label: 'Number of Equipment',
          data: counts,
          backgroundColor: [
            'rgba(52, 152, 219, 0.8)',
            'rgba(46, 204, 113, 0.8)',
            'rgba(155, 89, 182, 0.8)',
            'rgba(241, 196, 15, 0.8)',
            'rgba(231, 76, 60, 0.8)',
          ],
          borderColor: [
            'rgba(52, 152, 219, 1)',
            'rgba(46, 204, 113, 1)',
            'rgba(155, 89, 182, 1)',
            'rgba(241, 196, 15, 1)',
            'rgba(231, 76, 60, 1)',
          ],
          borderWidth: 2,
        },
      ],
    };
  };

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: {
        display: false,
      },
      title: {
        display: true,
        text: 'Equipment Distribution by Type',
        font: {
          size: 16,
        },
      },
    },
    scales: {
      y: {
        beginAtZero: true,
        ticks: {
          stepSize: 1,
        },
      },
    },
  };

  return (
    <div className="App">
      {/* Header */}
      <div className="header">
        <h1>Chemical Equipment Parameter Visualizer</h1>
        <p>Upload your CSV file to analyze equipment data instantly</p>
      </div>

      {/* Upload Section */}
      <div className="upload-section">
        <h2>Upload CSV File</h2>
        <div className="file-input-container">
          <input
            type="file"
            accept=".csv"
            onChange={handleFileChange}
            className="file-input"
          />
          <button
            onClick={handleSubmit}
            disabled={loading}
            className="upload-button"
          >
            {loading ? 'Processing...' : 'Analyze Data'}
          </button>
        </div>
        {selectedFile && (
          <p style={{ marginTop: '10px', color: '#27ae60' }}>
            Selected: {selectedFile.name}
          </p>
        )}
      </div>

      {/* Error Message */}
      {error && (
        <div className="error-message">
          <strong>Error:</strong> {error}
        </div>
      )}

      {/* Loading Indicator */}
      {loading && (
        <div className="loading">
          <p>Processing your CSV file...</p>
        </div>
      )}

      {/* Results Section */}
      {results && !loading && (
        <div className="results-container">
          <h2>Analysis Results</h2>

          {/* Statistics Grid */}
          <div className="stats-grid">
            <div className="stat-card">
              <h3>Total Equipment</h3>
              <p>{results.total_equipment}</p>
            </div>
            <div className="stat-card">
              <h3>Avg Flowrate</h3>
              <p>{results.average_flowrate}</p>
            </div>
            <div className="stat-card">
              <h3>Avg Pressure</h3>
              <p>{results.average_pressure}</p>
            </div>
            <div className="stat-card">
              <h3>Avg Temperature</h3>
              <p>{results.average_temperature}</p>
            </div>
          </div>

          {/* Chart Section */}
          <div className="chart-section">
            <h3>Equipment Distribution</h3>
            {getChartData() && (
              <Bar data={getChartData()} options={chartOptions} />
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;