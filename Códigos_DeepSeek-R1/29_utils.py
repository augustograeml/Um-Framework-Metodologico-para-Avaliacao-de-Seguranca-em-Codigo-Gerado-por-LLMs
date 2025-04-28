def print_repositories(repositories):
    if not repositories:
        print("No repositories found.")
        return

    for repo in repositories:
        name = repo.get('name')
        description = repo.get('description', 'No description provided.')
        url = repo.get('html_url')
        print(f"Repository Name: {name}")
        print(f"Description: {description}")
        print(f"URL: {url}")
        print("-" * 40)