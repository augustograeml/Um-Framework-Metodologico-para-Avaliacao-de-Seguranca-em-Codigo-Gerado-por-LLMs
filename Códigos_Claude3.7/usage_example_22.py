from config_system.config_manager import ConfigManager
from config_system.serializers.json_serializer import JsonSerializer
from config_system.serializers.yaml_serializer import YamlSerializer
from config_system.loaders.file_loader import FileLoader

def main():
    # Create an instance of ConfigManager
    config_manager = ConfigManager()

    # Load a JSON configuration file
    json_loader = FileLoader()
    json_serializer = JsonSerializer()
    json_config = json_loader.load('examples/sample_config.json', json_serializer)
    print("Loaded JSON Config:", json_config)

    # Load a YAML configuration file
    yaml_loader = FileLoader()
    yaml_serializer = YamlSerializer()
    yaml_config = yaml_loader.load('examples/sample_config.yaml', yaml_serializer)
    print("Loaded YAML Config:", yaml_config)

    # Validate the loaded configurations (assuming validate_schema is defined)
    # config_manager.validate_config(json_config)
    # config_manager.validate_config(yaml_config)

if __name__ == "__main__":
    main()