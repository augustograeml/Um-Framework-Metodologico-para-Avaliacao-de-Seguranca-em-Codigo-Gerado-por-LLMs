class APIClient:
    def __init__(self):
        pass

    def get_data(self, endpoint: str):
        import requests
        response = requests.get(endpoint)
        response.raise_for_status()
        return response.json()

    def post_data(self, endpoint: str, data: dict):
        import requests
        response = requests.post(endpoint, json=data)
        response.raise_for_status()
        return response.json()