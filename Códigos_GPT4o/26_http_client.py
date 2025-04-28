class HttpClient:
    import requests

    @staticmethod
    def get(url):
        response = HttpClient.requests.get(url)
        return response

    @staticmethod
    def post(url, data):
        response = HttpClient.requests.post(url, json=data)
        return response