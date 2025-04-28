class ConfigManager:
    def __init__(self, default_config_path):
        self.default_config_path = default_config_path
        self.current_config = {}

    def load_config(self, config_path):
        import json
        from src.utils.file_utils import read_json

        try:
            self.current_config = read_json(config_path)
        except FileNotFoundError:
            print(f"Configuration file not found: {config_path}. Loading default configuration.")
            self.current_config = read_json(self.default_config_path)

    def save_config(self, config_path):
        from src.utils.file_utils import write_json

        write_json(config_path, self.current_config)