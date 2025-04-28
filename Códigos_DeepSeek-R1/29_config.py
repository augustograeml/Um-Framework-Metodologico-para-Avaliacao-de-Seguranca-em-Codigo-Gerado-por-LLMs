def load_config():
    import os
    from dotenv import load_dotenv

    load_dotenv()  # Load environment variables from .env file

    return {
        "GITHUB_PAT": os.getenv("GITHUB_PAT")
    }