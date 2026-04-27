import pandas as pd

class Repository: # Store the data and load data
    def __init__(self, file_path="../../data/final_dataset.csv"):
        self.file_path = file_path  # Store the CSV file path

    def save(self, df):
        df.to_csv(self.file_path, index=False)

    def load(self):
        return pd.read_csv(self.file_path)