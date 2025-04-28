import os
from github_client import GitHubClient
from config import load_config

def main():
    config = load_config()
    token = config.get("GITHUB_TOKEN")
    username = input("Enter the GitHub username: ")

    client = GitHubClient(token)
    repositories = client.get_user_repositories(username)

    if repositories:
        print(f"Repositories for user {username}:")
        for repo in repositories:
            print(f"- {repo['name']}: {repo['html_url']}")
    else:
        print(f"No repositories found for user {username}.")

if __name__ == "__main__":
    main()