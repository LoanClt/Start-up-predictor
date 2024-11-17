from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout
from tabs.map_tab import MapTab
from tabs.data_tab import DataTab
from tabs.network_tab import NetworkTab
from tabs.prediction_tab import PredictionTab
from tabs.investment_analysis_tab import InvestmentAnalysisTab  # Add this import

class MainWindow(QMainWindow):
  def __init__(self):
      super().__init__()
      self.setWindowTitle("Startup Analysis Tool")
      self.setGeometry(100, 100, 1200, 800)
      
      # Create main widget and layout
      main_widget = QWidget()
      self.setCentralWidget(main_widget)
      layout = QVBoxLayout(main_widget)
      
      # Create tab widget
      tabs = QTabWidget()
      
      # Add tabs
      tabs.addTab(MapTab(), "Startup Map")
      tabs.addTab(DataTab(), "Data Explorer")
      tabs.addTab(NetworkTab(), "Network Analysis")
      tabs.addTab(PredictionTab(), "Success Prediction")
      tabs.addTab(InvestmentAnalysisTab(), "Investment Analysis")  # Add new tab
      
      layout.addWidget(tabs)