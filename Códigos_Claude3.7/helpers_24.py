def validate_json(data):
    if not isinstance(data, dict):
        raise ValueError("Invalid JSON data: Expected a dictionary.")

def format_data(data):
    return {key: str(value) for key, value in data.items()}