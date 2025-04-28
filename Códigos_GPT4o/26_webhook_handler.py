class WebhookHandler:
    def handle_webhook(self, url):
        import requests
        
        try:
            response = requests.get(url)
            return response.status_code, response.text
        except requests.exceptions.RequestException as e:
            return str(e), None