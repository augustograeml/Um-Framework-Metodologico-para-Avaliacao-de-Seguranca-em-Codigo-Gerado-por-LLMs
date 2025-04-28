import sys
from api.client import ApiClient
from utils.helpers import validate_url

def main():
    endpoint = input("Please enter the API endpoint URL: ")
    
    if not validate_url(endpoint):
        print("Invalid URL. Please try again.")
        sys.exit(1)

    client = ApiClient()
    data = client.fetch_data(endpoint)

    if data:
        print("Data retrieved successfully:")
        print(data)
    else:
        print("No data found or an error occurred.")

if __name__ == "__main__":
    main()