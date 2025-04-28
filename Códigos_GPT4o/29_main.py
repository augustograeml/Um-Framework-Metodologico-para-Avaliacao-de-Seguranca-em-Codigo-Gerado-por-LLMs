import os
from api.github_client import GitHubClient
from utils.config import load_config

def main():
    config = load_config()
    token = config.get('GITHUB_TOKEN')

    if not token:
        print("Error: GitHub Personal Access Token not found in configuration.")
        return

    client = GitHubClient(token)

    username = input("Enter the GitHub username to fetch repositories: ")
    repositories = client.get_user_repositories(username)

    if repositories:
        print(f"Repositories for user '{username}':")
        for repo in repositories:
            print(f"- {repo['name']}: {repo['html_url']}")
    else:
        print(f"No repositories found for user '{username}'.")

if __name__ == "__main__":
    main()