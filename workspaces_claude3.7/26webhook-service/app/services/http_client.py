class HttpClient:
    import requests

    @staticmethod
    def get(url):
        try:
            response = HttpClient.requests.get(url)
            response.raise_for_status()
            return response.json()
        except HttpClient.requests.RequestException as e:
            return {"error": str(e)}

    @staticmethod
    def post(url, data=None):
        try:
            response = HttpClient.requests.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except HttpClient.requests.RequestException as e:
            return {"error": str(e)}