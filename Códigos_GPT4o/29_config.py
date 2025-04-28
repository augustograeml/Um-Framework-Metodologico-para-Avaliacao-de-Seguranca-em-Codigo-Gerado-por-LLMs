def load_config():
    import os
    from dotenv import load_dotenv

    load_dotenv()  # Load environment variables from a .env file if it exists

    personal_access_token = os.getenv("GITHUB_PAT")
    
    if not personal_access_token:
        raise ValueError("Personal Access Token (GITHUB_PAT) not found in environment variables.")

    return {
        "GITHUB_PAT": personal_access_token
    }