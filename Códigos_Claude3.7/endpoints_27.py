from urllib.parse import urljoin

BASE_URL = "https://api.example.com/"

ENDPOINTS = {
    "users": "v1/users/",
    "posts": "v1/posts/",
    "comments": "v1/comments/",
}

def get_endpoint(name: str) -> str:
    if name in ENDPOINTS:
        return urljoin(BASE_URL, ENDPOINTS[name])
    else:
        raise ValueError(f"Endpoint '{name}' not found.")