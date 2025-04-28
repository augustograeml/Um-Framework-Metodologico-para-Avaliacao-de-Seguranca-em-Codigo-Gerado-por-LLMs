class Downloader:
    def download(self, url):
        import requests
        
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.content

    def save_file(self, content, filename):
        with open(filename, 'wb') as file:
            file.write(content)