from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QFormLayout, QLineEdit,
                           QPushButton, QLabel)
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from data_loader import DataLoader

class PredictionTab(QWidget):
    def __init__(self):
        super().__init__()
        self.data_loader = DataLoader()
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        
        # Create form for input
        form = QFormLayout()
        
        self.university = QLineEdit()
        form.addRow("University:", self.university)
        
        self.connections = QLineEdit()
        form.addRow("Number of Connections:", self.connections)
        
        self.experience = QLineEdit()
        form.addRow("Years of Experience:", self.experience)
        
        layout.addLayout(form)
        
        # Prediction button
        predict_btn = QPushButton("Predict Success")
        predict_btn.clicked.connect(self.predict_success)
        layout.addWidget(predict_btn)
        
        # Result label
        self.result_label = QLabel()
        layout.addWidget(self.result_label)
        
    def predict_success(self):
        # This is a simplified prediction model
        connections = int(self.connections.text() or 0)
        experience = int(self.experience.text() or 0)
        
        # Simple rule-based prediction
        score = (connections * 0.6 + experience * 0.4) / 10
        
        self.result_label.setText(f"Predicted Success Rate: {score:.1f}/10")
