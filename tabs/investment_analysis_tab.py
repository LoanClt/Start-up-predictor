from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QComboBox, 
                          QPushButton, QLabel)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from data_loader import DataLoader

class InvestmentAnalysisTab(QWidget):
  def __init__(self):
      super().__init__()
      self.data_loader = DataLoader()
      self.data_loader.load_data()
      self.init_ui()
      
  def init_ui(self):
      layout = QVBoxLayout(self)
      
      # Controls
      controls_layout = QHBoxLayout()
      
      # Analysis type selector
      self.analysis_selector = QComboBox()
      self.analysis_selector.addItems([
          'Investment Amounts Over Time',
          'Investment Rounds Distribution',
          'Average Investment by Category',
          'Geographic Investment Distribution',
          'Investment Growth Rate'
      ])
      controls_layout.addWidget(self.analysis_selector)
      
      # Update button
      update_btn = QPushButton("Update Analysis")
      update_btn.clicked.connect(self.update_analysis)
      controls_layout.addWidget(update_btn)
      
      layout.addLayout(controls_layout)
      
      # Matplotlib figure
      self.figure, self.ax = plt.subplots(figsize=(10, 6))
      self.canvas = FigureCanvas(self.figure)
      layout.addWidget(self.canvas)
      
      # Initial plot
      self.update_analysis()
      
  def update_analysis(self):
      analysis_type = self.analysis_selector.currentText()
      self.ax.clear()
      
      if analysis_type == 'Investment Amounts Over Time':
          self.plot_investment_trends()
      elif analysis_type == 'Investment Rounds Distribution':
          self.plot_round_distribution()
      elif analysis_type == 'Average Investment by Category':
          self.plot_category_averages()
      elif analysis_type == 'Geographic Investment Distribution':
          self.plot_geographic_distribution()
      elif analysis_type == 'Investment Growth Rate':
          self.plot_growth_rate()
          
      self.canvas.draw()
      
  def plot_investment_trends(self):
      # Convert funding_rounds data to time series
      df = self.data_loader.funding_rounds
      df['funded_at'] = pd.to_datetime(df['funded_at'])
      df = df.set_index('funded_at')
      
      # Resample by month and sum investments
      monthly_investments = df['raised_amount_usd'].resample('ME').sum()
      
      # Plot
      self.ax.plot(monthly_investments.index, monthly_investments.values)
      self.ax.set_title('Monthly Investment Trends')
      self.ax.set_xlabel('Date')
      self.ax.set_ylabel('Total Investment (USD)')
      plt.xticks(rotation=45)
      
  def plot_round_distribution(self):
      df = self.data_loader.funding_rounds
      round_counts = df['funding_round_type'].value_counts()
      
      # Plot
      round_counts.plot(kind='bar', ax=self.ax)
      self.ax.set_title('Distribution of Investment Rounds')
      self.ax.set_xlabel('Round Type')
      self.ax.set_ylabel('Count')
      plt.xticks(rotation=45)
      
  def plot_category_averages(self):
      df = self.data_loader.funding_rounds
      avg_by_type = df.groupby('funding_round_type')['raised_amount_usd'].mean()
      
      # Plot
      avg_by_type.plot(kind='bar', ax=self.ax)
      self.ax.set_title('Average Investment by Round Type')
      self.ax.set_xlabel('Round Type')
      self.ax.set_ylabel('Average Amount (USD)')
      plt.xticks(rotation=45)
      
  def plot_geographic_distribution(self):
      # Merge funding rounds with offices data
      df = pd.merge(
          self.data_loader.funding_rounds,
          self.data_loader.offices[['object_id', 'country_code']],
          left_on='object_id',
          right_on='object_id'
      )
      
      country_totals = df.groupby('country_code')['raised_amount_usd'].sum()
      
      # Plot
      country_totals.plot(kind='bar', ax=self.ax)
      self.ax.set_title('Total Investment by Country')
      self.ax.set_xlabel('Country')
      self.ax.set_ylabel('Total Investment (USD)')
      plt.xticks(rotation=45)
      
  def plot_growth_rate(self):
      df = self.data_loader.funding_rounds
      df['funded_at'] = pd.to_datetime(df['funded_at'])
      df = df.set_index('funded_at')
      
      # Calculate year-over-year growth rate
      yearly_investments = df['raised_amount_usd'].resample('Y').sum()
      growth_rate = yearly_investments.pct_change() * 100
      
      # Plot
      self.ax.plot(growth_rate.index, growth_rate.values)
      self.ax.set_title('Year-over-Year Investment Growth Rate')
      self.ax.set_xlabel('Year')
      self.ax.set_ylabel('Growth Rate (%)')
      plt.xticks(rotation=45)