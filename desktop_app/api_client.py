"""
API Client for Django Backend Communication

This module handles all HTTP communication with the Django backend.
It sends CSV files to the backend and receives JSON responses.

The backend must be running at http://localhost:8000
"""

import requests


class EquipmentAnalyzerAPI:
    """
    Client for communicating with the Equipment Analyzer backend API.
    """
    
    def __init__(self, base_url="http://localhost:8000"):
        """
        Initialize API client with backend URL.
        
        Args:
            base_url (str): Base URL of Django backend
        """
        self.base_url = base_url
        self.analyze_endpoint = f"{base_url}/api/analyze/"
    
    def upload_and_analyze_csv(self, file_path):
        """
        Upload CSV file to backend and get analysis results.
        
        Args:
            file_path (str): Full path to CSV file
            
        Returns:
            dict: JSON response from backend with statistics
                {
                    'total_equipment': int,
                    'average_flowrate': float,
                    'average_pressure': float,
                    'average_temperature': float,
                    'equipment_by_type': dict
                }
                
        Raises:
            ConnectionError: If backend is not reachable
            requests.exceptions.RequestException: For other HTTP errors
            ValueError: If backend returns an error response
        """
        try:
            # Open the CSV file in binary mode
            with open(file_path, 'rb') as csv_file:
                # Prepare the multipart form data
                # Key must be 'file' to match backend expectation
                files = {'file': csv_file}
                
                # Send POST request to Django backend
                response = requests.post(
                    self.analyze_endpoint,
                    files=files,
                    timeout=10  # 10 second timeout
                )
                
                # Check if request was successful
                if response.status_code == 200:
                    # Parse and return JSON response
                    return response.json()
                else:
                    # Backend returned an error
                    error_data = response.json()
                    error_message = error_data.get('error', 'Unknown error occurred')
                    raise ValueError(f"Backend error: {error_message}")
                    
        except requests.exceptions.ConnectionError:
            raise ConnectionError(
                "Cannot connect to backend server. "
                "Make sure Django is running on http://localhost:8000"
            )
        except requests.exceptions.Timeout:
            raise ConnectionError("Request timed out. Backend server is not responding.")
        except FileNotFoundError:
            raise FileNotFoundError(f"CSV file not found: {file_path}")
        except Exception as e:
            raise Exception(f"Error uploading file: {str(e)}")
    
    def check_backend_status(self):
        """
        Check if backend server is running.
        
        Returns:
            bool: True if backend is reachable, False otherwise
        """
        try:
            response = requests.get(self.base_url, timeout=2)
            return True
        except:
            return False


# Example usage (for testing)
if __name__ == "__main__":
    # This code runs only when this file is executed directly
    api = EquipmentAnalyzerAPI()
    
    # Check if backend is running
    if api.check_backend_status():
        print("✓ Backend is running")
    else:
        print("✗ Backend is not running")
        print("Start Django with: python manage.py runserver")