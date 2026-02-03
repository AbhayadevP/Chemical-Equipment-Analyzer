"""
Chemical Equipment Parameter Visualizer - Desktop Application
Main Entry Point

This is the entry point for the PyQt5 desktop application.
It initializes the Qt application and displays the main window.

Author: Desktop Application Team
Version: 1.0.0
"""

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from ui_main import MainWindow


def main():
    """
    Main function to launch the desktop application.
    """
    # Enable high DPI scaling for better display on high-resolution screens
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    
    # Create Qt application instance
    # sys.argv allows passing command-line arguments to the app
    app = QApplication(sys.argv)
    
    # Set application metadata
    app.setApplicationName("Chemical Equipment Parameter Visualizer")
    app.setOrganizationName("Equipment Analytics")
    app.setApplicationVersion("1.0.0")
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    # Print startup message to console
    print("=" * 60)
    print("Chemical Equipment Parameter Visualizer - Desktop")
    print("=" * 60)
    print("✓ Application started successfully")
    print("✓ Make sure Django backend is running on http://localhost:8000")
    print("=" * 60)
    
    # Start the application event loop
    # This keeps the app running until the user closes it
    # sys.exit() ensures proper cleanup on exit
    sys.exit(app.exec_())


if __name__ == "__main__":
    """
    This block runs only when the script is executed directly,
    not when imported as a module.
    """
    main()