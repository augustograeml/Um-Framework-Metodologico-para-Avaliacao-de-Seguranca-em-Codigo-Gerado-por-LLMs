import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_API_URL = "https://api.github.com"
PERSONAL_ACCESS_TOKEN = os.getenv("GITHUB_PAT")  # Load the Personal Access Token from environment variables

if not PERSONAL_ACCESS_TOKEN:
    raise ValueError("Personal Access Token (GITHUB_PAT) not found in environment variables.")