import sys
from api_integration.client import APIClient
from api_integration.auth import Auth
from api_integration.config import Config
from api_integration.endpoints import get_endpoint

def main():
    config = Config()
    auth = Auth()
    client = APIClient()

    # Authenticate and get token
    auth.authenticate()
    token = auth.get_token()
    
    # Set the token in the client
    client.set_token(token)

    # User input for endpoint
    endpoint_name = input("Enter the endpoint name: ")
    endpoint = get_endpoint(endpoint_name)

    # Retrieve data from the specified endpoint
    data = client.get_data(endpoint)
    
    # Output the retrieved data
    print("Retrieved data:", data)

if __name__ == "__main__":
    main()