class URLDownloader:
    def __init__(self):
        pass

    def download(self, url: str, save_path: str) -> bool:
        import requests

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            with open(save_path, 'wb') as file:
                file.write(response.content)
            return True
        except Exception as e:
            print(f"An error occurred while downloading: {e}")
            return False