from PyQt5.QtWidgets import QWidget, QVBoxLayout
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from data_loader import DataLoader

class NetworkTab(QWidget):
    def __init__(self):
        super().__init__()
        self.data_loader = DataLoader()
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        
        # Create the network visualization
        figure = plt.figure(figsize=(10, 8))
        canvas = FigureCanvas(figure)
        layout.addWidget(canvas)
        
        # Load and display network
        self.data_loader.load_data()
        self.create_network(figure)
        
    def create_network(self, figure):
        # Create network from relationships data
        G = nx.Graph()
        
        # Add nodes and edges from relationships
        if self.data_loader.relationships is not None:
            for _, row in self.data_loader.relationships.iterrows():
                G.add_edge(row['person_object_id'], row['relationship_object_id'])
        
        # Draw network
        plt.clf()
        nx.draw(G, with_labels=True, node_size=500, node_color='lightblue',
                font_size=8, font_weight='bold')
        plt.title("Startup Founder Network")
