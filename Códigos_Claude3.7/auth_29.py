def load_token(env_file='.env'):
    """Load the Personal Access Token from the specified .env file."""
    from dotenv import load_dotenv
    import os

    load_dotenv(env_file)
    token = os.getenv('GITHUB_PAT')

    if not token:
        raise ValueError("Personal Access Token (GITHUB_PAT) not found in the environment variables.")
    
    return token