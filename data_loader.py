import pandas as pd

class DataLoader:
    def __init__(self):
        self.companies = None
        self.people = None
        self.relationships = None
        self.investments = None
        self.offices = None
        self.funding_rounds = None
        
    def load_data(self, n_rows=200):  # Add n_rows parameter with default None
        """Load all CSV files into pandas DataFrames
        Args:
            n_rows (int, optional): Number of rows to read from each file. If None, read all rows.
        """
        try:
            self.people = pd.read_csv('data/people.csv', nrows=n_rows)
            self.relationships = pd.read_csv('data/relationships.csv', nrows=n_rows)
            self.investments = pd.read_csv('data/investments.csv', nrows=n_rows)
            self.offices = pd.read_csv('data/offices.csv', nrows=n_rows)
            self.funding_rounds = pd.read_csv('data/funding_rounds.csv', nrows=n_rows)
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
    
    def get_startup_locations(self):
        """Return offices data for mapping"""
        if self.offices is not None:
            return self.offices[['object_id', 'city', 'state_code', 'country_code', 
                                'latitude', 'longitude', 'region']].dropna(subset=['latitude', 'longitude'])
        return pd.DataFrame()