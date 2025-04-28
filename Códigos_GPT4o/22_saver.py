class Saver:
    def __init__(self):
        self.saved_configs = {}

    def save_config(self, file_path, config):
        with open(file_path, 'w') as file:
            file.write(self.serialize(config))
        self.saved_configs[file_path] = config

    def get_saved_configs(self):
        return list(self.saved_configs.keys())

    def serialize(self, data):
        import json
        return json.dumps(data)

    def deserialize(self, data):
        import json
        return json.loads(data)