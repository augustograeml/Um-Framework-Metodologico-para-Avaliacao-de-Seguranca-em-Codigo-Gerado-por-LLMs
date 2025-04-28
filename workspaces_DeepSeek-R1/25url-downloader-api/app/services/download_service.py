class DownloadService:
    def download(self, url: str, save_path: str) -> str:
        import requests

        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            return f"Downloaded content from {url} to {save_path}"
        else:
            raise Exception(f"Failed to download content from {url}. Status code: {response.status_code}")