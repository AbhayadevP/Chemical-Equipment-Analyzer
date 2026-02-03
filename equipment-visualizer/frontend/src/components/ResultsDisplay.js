import React from 'react';
import './ResultsDisplay.css';
import EquipmentTypeChart from './EquipmentTypeChart';

function ResultsDisplay({ data }) {
  if (!data) {
    return null;
  }

  return (
    <div className="results-container">
      <h2>Analysis Results</h2>
      
      <div className="stats-grid">
        <div className="stat-card">
          <div className="stat-label">Total Equipment</div>
          <div className="stat-value">{data.total_equipment}</div>
        </div>
        
        <div className="stat-card">
          <div className="stat-label">Average Flowrate</div>
          <div className="stat-value">
            {data.average_flowrate !== null && data.average_flowrate !== undefined
              ? data.average_flowrate.toFixed(2)
              : 'N/A'}
          </div>
        </div>
        
        <div className="stat-card">
          <div className="stat-label">Average Pressure</div>
          <div className="stat-value">
            {data.average_pressure !== null && data.average_pressure !== undefined
              ? data.average_pressure.toFixed(2)
              : 'N/A'}
          </div>
        </div>
        
        <div className="stat-card">
          <div className="stat-label">Average Temperature</div>
          <div className="stat-value">
            {data.average_temperature !== null && data.average_temperature !== undefined
              ? data.average_temperature.toFixed(2)
              : 'N/A'}
          </div>
        </div>
      </div>

      <div className="equipment-type-section">
        <h3>Equipment Distribution by Type</h3>
        <div className="equipment-type-list">
          {data.equipment_per_type && Object.entries(data.equipment_per_type).map(([type, count]) => (
            <div key={type} className="equipment-type-item">
              <span className="equipment-type-name">{type}</span>
              <span className="equipment-type-count">{count}</span>
            </div>
          ))}
        </div>
      </div>

      <div className="chart-section">
        <h3>Equipment Type Distribution Chart</h3>
        <EquipmentTypeChart data={data.equipment_per_type} />
      </div>
    </div>
  );
}

export default ResultsDisplay;
