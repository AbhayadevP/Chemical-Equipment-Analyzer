import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';
import './EquipmentTypeChart.css';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

function EquipmentTypeChart({ data }) {
  if (!data || Object.keys(data).length === 0) {
    return <p>No data available for chart</p>;
  }

  const chartData = {
    labels: Object.keys(data),
    datasets: [
      {
        label: 'Number of Equipment',
        data: Object.values(data),
        backgroundColor: [
          'rgba(76, 175, 80, 0.8)',
          'rgba(33, 150, 243, 0.8)',
          'rgba(255, 152, 0, 0.8)',
          'rgba(156, 39, 176, 0.8)',
          'rgba(244, 67, 54, 0.8)',
        ],
        borderColor: [
          'rgba(76, 175, 80, 1)',
          'rgba(33, 150, 243, 1)',
          'rgba(255, 152, 0, 1)',
          'rgba(156, 39, 176, 1)',
          'rgba(244, 67, 54, 1)',
        ],
        borderWidth: 1,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: {
        display: true,
        position: 'top',
      },
      title: {
        display: false,
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
    <div className="chart-container">
      <Bar data={chartData} options={options} />
    </div>
  );
}

export default EquipmentTypeChart;
