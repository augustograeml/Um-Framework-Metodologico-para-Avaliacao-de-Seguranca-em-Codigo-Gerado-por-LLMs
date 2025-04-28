import os
from api.github_client import GitHubClient
from utils.auth import load_token

def main():
    token = load_token()
    client = GitHubClient()
    client.authenticate(token)

    username = input("Enter the GitHub username: ")
    repositories = client.get_user_repositories(username)

    if repositories:
        print(f"Repositories for user {username}:")
        for repo in repositories:
            print(f"- {repo.name}: {repo.url} - {repo.description}")
    else:
        print(f"No repositories found for user {username}.")

if __name__ == "__main__":
    main()