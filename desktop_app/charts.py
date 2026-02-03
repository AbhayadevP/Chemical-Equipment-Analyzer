"""
Chart Generation Module

This module creates Matplotlib charts for displaying equipment data.
Charts are embedded directly into PyQt5 windows.
"""

import matplotlib
matplotlib.use('Qt5Agg')  # Use Qt5 backend for PyQt5 integration

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class EquipmentDistributionChart(FigureCanvas):
    """
    A bar chart showing equipment distribution by type.
    
    This class inherits from FigureCanvas, making it a PyQt5 widget
    that can be embedded directly in the application window.
    """
    
    def __init__(self, parent=None, width=8, height=5, dpi=100):
        """
        Initialize the chart canvas.
        
        Args:
            parent: Parent Qt widget
            width (int): Figure width in inches
            height (int): Figure height in inches
            dpi (int): Dots per inch (resolution)
        """
        # Create matplotlib figure
        self.figure = Figure(figsize=(width, height), dpi=dpi)
        
        # Initialize the canvas
        super().__init__(self.figure)
        
        # Set parent widget
        self.setParent(parent)
        
        # Create the subplot (axis)
        self.axes = self.figure.add_subplot(111)
    
    def plot_equipment_distribution(self, equipment_by_type):
        """
        Plot equipment distribution as a bar chart.
        
        Args:
            equipment_by_type (dict): Dictionary mapping equipment type to count
                Example: {'Pump': 10, 'Reactor': 9, 'Heater': 6}
        """
        # Clear previous plot
        self.axes.clear()
        
        if not equipment_by_type:
            # No data to plot
            self.axes.text(
                0.5, 0.5, 'No data available',
                horizontalalignment='center',
                verticalalignment='center',
                transform=self.axes.transAxes,
                fontsize=14,
                color='gray'
            )
            self.draw()
            return
        
        # Extract equipment types and counts
        types = list(equipment_by_type.keys())
        counts = list(equipment_by_type.values())
        
        # Define colors for bars
        colors = [
            '#3498db',  # Blue
            '#2ecc71',  # Green
            '#9b59b6',  # Purple
            '#f39c12',  # Orange
            '#e74c3c',  # Red
            '#1abc9c',  # Turquoise
            '#34495e',  # Dark gray
        ]
        
        # Create bar chart
        bars = self.axes.bar(
            types,
            counts,
            color=colors[:len(types)],
            edgecolor='black',
            linewidth=1.2,
            alpha=0.8
        )
        
        # Customize the chart
        self.axes.set_xlabel('Equipment Type', fontsize=12, fontweight='bold')
        self.axes.set_ylabel('Number of Equipment', fontsize=12, fontweight='bold')
        self.axes.set_title(
            'Equipment Distribution by Type',
            fontsize=14,
            fontweight='bold',
            pad=20
        )
        
        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            self.axes.text(
                bar.get_x() + bar.get_width() / 2.0,
                height,
                f'{int(height)}',
                ha='center',
                va='bottom',
                fontsize=10,
                fontweight='bold'
            )
        
        # Set y-axis to start at 0 and use integer ticks
        self.axes.set_ylim(bottom=0)
        
        # Make y-axis show only integers
        import matplotlib.ticker as ticker
        self.axes.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
        
        # Rotate x-axis labels if there are many types
        if len(types) > 4:
            self.axes.tick_params(axis='x', rotation=45)
        
        # Add grid for better readability
        self.axes.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Tight layout to prevent label cutoff
        self.figure.tight_layout()
        
        # Redraw the canvas
        self.draw()
    
    def clear_chart(self):
        """Clear the chart."""
        self.axes.clear()
        self.draw()


# Example usage (for testing)
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
    
    # Create Qt application
    app = QApplication(sys.argv)
    
    # Create main window
    window = QMainWindow()
    window.setWindowTitle("Chart Test")
    
    # Create central widget with layout
    central_widget = QWidget()
    layout = QVBoxLayout()
    central_widget.setLayout(layout)
    window.setCentralWidget(central_widget)
    
    # Create and add chart
    chart = EquipmentDistributionChart(central_widget)
    layout.addWidget(chart)
    
    # Plot sample data
    sample_data = {
        'Pump': 10,
        'Reactor': 9,
        'Heater': 6,
        'Mixer': 3
    }
    chart.plot_equipment_distribution(sample_data)
    
    # Show window
    window.resize(800, 600)
    window.show()
    
    sys.exit(app.exec_())