class Config:
    def __init__(self, config_file='config/default.yaml'):
        import yaml
        with open(config_file, 'r') as file:
            self.settings = yaml.safe_load(file)

    def get_setting(self, key: str):
        return self.settings.get(key)