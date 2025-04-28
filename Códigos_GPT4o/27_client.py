class ApiClient:
    def __init__(self):
        pass

    def fetch_data(self, endpoint):
        import requests

        if not self.validate_url(endpoint):
            raise ValueError("Invalid URL provided.")

        response = requests.get(endpoint)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()

    def validate_url(self, url):
        from urllib.parse import urlparse

        parsed = urlparse(url)
        return all([parsed.scheme, parsed.netloc])