"""
Main UI Module for Desktop Application

This module contains the main window and all UI components.
It handles user interactions and displays results from the backend.
"""

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFileDialog, QGroupBox,
    QGridLayout, QMessageBox, QFrame
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont

from api_client import EquipmentAnalyzerAPI
from charts import EquipmentDistributionChart


class UploadWorker(QThread):
    """
    Background thread for uploading CSV to backend.
    
    This prevents the UI from freezing during file upload.
    """
    
    # Signals to communicate with main thread
    upload_complete = pyqtSignal(dict)  # Emits results when successful
    upload_error = pyqtSignal(str)      # Emits error message on failure
    
    def __init__(self, api_client, file_path):
        super().__init__()
        self.api_client = api_client
        self.file_path = file_path
    
    def run(self):
        """
        This method runs in background thread.
        """
        try:
            # Upload CSV and get results
            results = self.api_client.upload_and_analyze_csv(self.file_path)
            # Emit success signal with results
            self.upload_complete.emit(results)
        except Exception as e:
            # Emit error signal with error message
            self.upload_error.emit(str(e))


class MainWindow(QMainWindow):
    """
    Main application window for Chemical Equipment Parameter Visualizer.
    """
    
    def __init__(self):
        super().__init__()
        
        # Initialize API client
        self.api_client = EquipmentAnalyzerAPI()
        
        # Initialize UI
        self.init_ui()
        
        # Store current file path
        self.current_file_path = None
        
        # Background worker thread
        self.upload_worker = None
    
    def init_ui(self):
        """
        Initialize and layout all UI components.
        """
        # Set window properties
        self.setWindowTitle("Chemical Equipment Parameter Visualizer - Desktop")
        self.setGeometry(100, 100, 1000, 800)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Add components
        main_layout.addWidget(self.create_header())
        main_layout.addWidget(self.create_upload_section())
        main_layout.addWidget(self.create_status_section())
        main_layout.addWidget(self.create_results_section())
        main_layout.addWidget(self.create_chart_section())
        
        # Add stretch to push everything to top
        main_layout.addStretch()
    
    def create_header(self):
        """
        Create header section with title.
        """
        header_frame = QFrame()
        header_frame.setStyleSheet("""
            QFrame {
                background-color: #2c3e50;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        
        header_layout = QVBoxLayout()
        header_frame.setLayout(header_layout)
        
        # Title label
        title_label = QLabel("Chemical Equipment Parameter Visualizer")
        title_font = QFont("Arial", 18, QFont.Bold)
        title_label.setFont(title_font)
        title_label.setStyleSheet("color: white;")
        title_label.setAlignment(Qt.AlignCenter)
        
        # Subtitle label
        subtitle_label = QLabel("Desktop Application - Upload CSV to analyze equipment data")
        subtitle_font = QFont("Arial", 11)
        subtitle_label.setFont(subtitle_font)
        subtitle_label.setStyleSheet("color: #ecf0f1;")
        subtitle_label.setAlignment(Qt.AlignCenter)
        
        header_layout.addWidget(title_label)
        header_layout.addWidget(subtitle_label)
        
        return header_frame
    
    def create_upload_section(self):
        """
        Create file upload section with button.
        """
        group_box = QGroupBox("Upload CSV File")
        group_box.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                font-size: 14px;
                border: 2px solid #3498db;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
        """)
        
        layout = QVBoxLayout()
        group_box.setLayout(layout)
        
        # Select file button
        self.select_file_btn = QPushButton("📁 Select CSV File")
        self.select_file_btn.setMinimumHeight(40)
        self.select_file_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:disabled {
                background-color: #95a5a6;
            }
        """)
        self.select_file_btn.clicked.connect(self.select_csv_file)
        
        # Selected file label
        self.selected_file_label = QLabel("No file selected")
        self.selected_file_label.setStyleSheet("color: #7f8c8d; font-style: italic;")
        
        layout.addWidget(self.select_file_btn)
        layout.addWidget(self.selected_file_label)
        
        return group_box
    
    def create_status_section(self):
        """
        Create status message section.
        """
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setMinimumHeight(30)
        self.status_label.setStyleSheet("""
            QLabel {
                font-size: 12px;
                padding: 5px;
                border-radius: 3px;
            }
        """)
        
        return self.status_label
    
    def create_results_section(self):
        """
        Create results display section with statistics.
        """
        group_box = QGroupBox("Analysis Results")
        group_box.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                font-size: 14px;
                border: 2px solid #2ecc71;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
        """)
        
        # Grid layout for statistics
        grid_layout = QGridLayout()
        group_box.setLayout(grid_layout)
        
        # Create stat cards
        stat_style = """
            QFrame {
                background-color: #ecf0f1;
                border-left: 4px solid #3498db;
                border-radius: 3px;
                padding: 10px;
            }
        """
        
        label_style = "color: #7f8c8d; font-size: 11px; font-weight: normal;"
        value_style = "color: #2c3e50; font-size: 20px; font-weight: bold;"
        
        # Total Equipment
        self.total_equipment_label = self.create_stat_card(
            "TOTAL EQUIPMENT", "—", stat_style, label_style, value_style
        )
        grid_layout.addWidget(self.total_equipment_label, 0, 0)
        
        # Average Flowrate
        self.avg_flowrate_label = self.create_stat_card(
            "AVERAGE FLOWRATE", "—", stat_style, label_style, value_style
        )
        grid_layout.addWidget(self.avg_flowrate_label, 0, 1)
        
        # Average Pressure
        self.avg_pressure_label = self.create_stat_card(
            "AVERAGE PRESSURE", "—", stat_style, label_style, value_style
        )
        grid_layout.addWidget(self.avg_pressure_label, 1, 0)
        
        # Average Temperature
        self.avg_temperature_label = self.create_stat_card(
            "AVERAGE TEMPERATURE", "—", stat_style, label_style, value_style
        )
        grid_layout.addWidget(self.avg_temperature_label, 1, 1)
        
        # Initially hide results section
        group_box.setVisible(False)
        self.results_group = group_box
        
        return group_box
    
    def create_stat_card(self, title, value, frame_style, label_style, value_style):
        """
        Create a single stat card frame.
        """
        frame = QFrame()
        frame.setStyleSheet(frame_style)
        
        layout = QVBoxLayout()
        frame.setLayout(layout)
        
        # Title label
        title_label = QLabel(title)
        title_label.setStyleSheet(label_style)
        
        # Value label
        value_label = QLabel(value)
        value_label.setStyleSheet(value_style)
        
        # Store value label for later updates
        frame.value_label = value_label
        
        layout.addWidget(title_label)
        layout.addWidget(value_label)
        
        return frame
    
    def create_chart_section(self):
        """
        Create chart display section.
        """
        group_box = QGroupBox("Equipment Distribution Chart")
        group_box.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                font-size: 14px;
                border: 2px solid #9b59b6;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
        """)
        
        layout = QVBoxLayout()
        group_box.setLayout(layout)
        
        # Create chart widget
        self.chart = EquipmentDistributionChart(group_box, width=8, height=4)
        layout.addWidget(self.chart)
        
        # Initially hide chart section
        group_box.setVisible(False)
        self.chart_group = group_box
        
        return group_box
    
    def select_csv_file(self):
        """
        Open file dialog to select CSV file and upload it.
        """
        # Check if backend is running first
        if not self.api_client.check_backend_status():
            QMessageBox.critical(
                self,
                "Backend Not Running",
                "Cannot connect to Django backend!\n\n"
                "Please start the backend server:\n"
                "python manage.py runserver\n\n"
                "Then try again."
            )
            return
        
        # Open file dialog
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select CSV File",
            "",
            "CSV Files (*.csv);;All Files (*)"
        )
        
        if file_path:
            # Store file path
            self.current_file_path = file_path
            
            # Update UI
            self.selected_file_label.setText(f"Selected: {file_path}")
            self.selected_file_label.setStyleSheet("color: #27ae60; font-weight: bold;")
            
            # Start upload
            self.upload_csv_file(file_path)
    
    def upload_csv_file(self, file_path):
        """
        Upload CSV file to backend in background thread.
        """
        # Disable upload button
        self.select_file_btn.setEnabled(False)
        
        # Show processing status
        self.show_status("Processing CSV file...", "info")
        
        # Hide previous results
        self.results_group.setVisible(False)
        self.chart_group.setVisible(False)
        
        # Create and start worker thread
        self.upload_worker = UploadWorker(self.api_client, file_path)
        self.upload_worker.upload_complete.connect(self.on_upload_success)
        self.upload_worker.upload_error.connect(self.on_upload_error)
        self.upload_worker.start()
    
    def on_upload_success(self, results):
        """
        Handle successful upload and display results.
        """
        # Re-enable upload button
        self.select_file_btn.setEnabled(True)
        
        # Show success status
        self.show_status("✓ Analysis complete!", "success")
        
        # Display results
        self.display_results(results)
    
    def on_upload_error(self, error_message):
        """
        Handle upload error.
        """
        # Re-enable upload button
        self.select_file_btn.setEnabled(True)
        
        # Show error status
        self.show_status(f"✗ Error: {error_message}", "error")
        
        # Show error dialog
        QMessageBox.critical(self, "Upload Error", error_message)
    
    def show_status(self, message, status_type):
        """
        Display status message with appropriate styling.
        """
        colors = {
            "info": "#3498db",
            "success": "#2ecc71",
            "error": "#e74c3c"
        }
        
        self.status_label.setText(message)
        self.status_label.setStyleSheet(f"""
            QLabel {{
                background-color: {colors.get(status_type, '#95a5a6')};
                color: white;
                font-size: 12px;
                font-weight: bold;
                padding: 8px;
                border-radius: 3px;
            }}
        """)
    
    def display_results(self, results):
        """
        Display analysis results in UI.
        
        Args:
            results (dict): Results from backend API
        """
        # Update statistics
        self.total_equipment_label.value_label.setText(str(results['total_equipment']))
        self.avg_flowrate_label.value_label.setText(f"{results['average_flowrate']:.2f}")
        self.avg_pressure_label.value_label.setText(f"{results['average_pressure']:.2f}")
        self.avg_temperature_label.value_label.setText(f"{results['average_temperature']:.2f}")
        
        # Show results section
        self.results_group.setVisible(True)
        
        # Plot chart
        self.chart.plot_equipment_distribution(results['equipment_by_type'])
        
        # Show chart section
        self.chart_group.setVisible(True)