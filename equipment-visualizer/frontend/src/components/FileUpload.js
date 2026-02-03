import React, { useRef } from 'react';
import axios from 'axios';
import './FileUpload.css';

const API_URL = 'http://localhost:8000/api/upload/';

function FileUpload({ onUploadStart, onUploadSuccess, onUploadError, loading }) {
  const fileInputRef = useRef(null);

  const handleFileChange = async (event) => {
    const file = event.target.files[0];
    
    if (!file) {
      return;
    }

    // Check if file is CSV
    if (!file.name.endsWith('.csv')) {
      onUploadError('Please upload a CSV file');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    onUploadStart();

    try {
      const response = await axios.post(API_URL, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      onUploadSuccess(response.data);
    } catch (error) {
      if (error.response && error.response.data && error.response.data.error) {
        onUploadError(error.response.data.error);
      } else {
        onUploadError('Failed to upload file. Please check if the backend server is running.');
      }
    }
  };

  const handleButtonClick = () => {
    fileInputRef.current?.click();
  };

  return (
    <div className="file-upload-container">
      <div className="file-upload-box">
        <input
          ref={fileInputRef}
          type="file"
          accept=".csv"
          onChange={handleFileChange}
          style={{ display: 'none' }}
          disabled={loading}
        />
        <button
          className="upload-button"
          onClick={handleButtonClick}
          disabled={loading}
        >
          {loading ? 'Processing...' : 'Select CSV File'}
        </button>
        <p className="upload-hint">
          Select a CSV file with equipment data (equipment_name, equipment_type, flowrate, pressure, temperature)
        </p>
      </div>
    </div>
  );
}

export default FileUpload;
