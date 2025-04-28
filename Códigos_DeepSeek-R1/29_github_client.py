class GitHubClient:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.github.com"

    def authenticate(self):
        headers = {
            "Authorization": f"token {self.token}"
        }
        return headers

    def get_user_repositories(self, username):
        headers = self.authenticate()
        url = f"{self.base_url}/users/{username}/repos"
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()