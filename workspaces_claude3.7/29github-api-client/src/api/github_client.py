class GitHubClient:
    def __init__(self):
        self.token = None

    def authenticate(self, token):
        self.token = token

    def get_user_repositories(self, username):
        import requests

        headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json',
        }
        url = f'https://api.github.com/users/{username}/repos'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()