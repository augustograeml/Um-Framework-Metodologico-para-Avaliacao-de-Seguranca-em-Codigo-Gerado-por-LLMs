def load_config():
    import os
    from dotenv import load_dotenv

    load_dotenv()  # Load environment variables from .env file

    config = {
        'API_KEY': os.getenv('API_KEY', 'your_default_api_key'),
        'BASE_URL': os.getenv('BASE_URL', 'https://api.example.com')
    }

    return config