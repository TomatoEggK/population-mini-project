import requests
import pandas as pd 

class ApiClient: # get data from API
    def __init__(self):
        self.base_url = "https://api.worldbank.org/v2"  # the API URL

    def fetch_indicator(self, indicator_code, per_page=500):
        all_records = []  # records from all pages

        first_url = f"{self.base_url}/country/all/indicator/{indicator_code}?format=json&per_page={per_page}&page=1"
        first_response = requests.get(first_url)  # Request the first page
        first_data = first_response.json()

        total_pages = first_data[0]["pages"]  # Get the total number of pages

        for page in range(1, total_pages + 1):
            url = f"{self.base_url}/country/all/indicator/{indicator_code}?format=json&per_page={per_page}&page={page}"
            response = requests.get(url)  # Request one page
            data = response.json()  # Convert to Python data

            records = data[1]  # Get the records
            all_records.extend(records)  # Add records

        return pd.DataFrame(all_records)  # Return as DataFrame

    def fetch_country_metadata(self, per_page=400):
        url = f"{self.base_url}/country?format=json&per_page={per_page}&page=1"
        response = requests.get(url)  # Request country metadata
        data = response.json() 

        records = data[1]
        return pd.DataFrame(records)