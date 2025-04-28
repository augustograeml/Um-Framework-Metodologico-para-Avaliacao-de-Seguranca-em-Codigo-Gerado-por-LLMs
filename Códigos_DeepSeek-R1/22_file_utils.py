def read_json(file_path):
    import json
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json(file_path, data):
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)