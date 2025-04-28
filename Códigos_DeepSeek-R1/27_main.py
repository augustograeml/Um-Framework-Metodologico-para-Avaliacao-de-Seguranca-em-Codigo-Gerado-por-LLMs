# main.py

import os
from api_integration import ApiIntegration
from config import load_config

def main():
    config = load_config()
    api_integration = ApiIntegration()

    endpoint = input("Please enter the API endpoint: ")
    response = api_integration.fetch_data(endpoint)

    if response:
        print("Data retrieved successfully.")
        # Further processing of the response can be done here
    else:
        print("Failed to retrieve data.")

if __name__ == "__main__":
    main()