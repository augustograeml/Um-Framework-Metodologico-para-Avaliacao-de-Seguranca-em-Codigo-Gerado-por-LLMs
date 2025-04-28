class YamlSerializer:
    def serialize(self, data):
        import yaml
        return yaml.dump(data)

    def deserialize(self, yaml_string):
        import yaml
        return yaml.load(yaml_string, Loader=yaml.FullLoader)