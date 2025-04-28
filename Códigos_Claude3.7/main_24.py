def main():
    import json
    from converter.json_importer import JsonImporter
    from converter.object_mapper import ObjectMapper
    from models.data_models import YourDataModel  # Replace with your actual data model

    # Initialize the JSON importer
    json_importer = JsonImporter()

    # Get the JSON file path from the user
    json_file_path = input("Enter the path to the JSON file: ")

    # Import JSON data
    try:
        data_dict = json_importer.import_json(json_file_path)
        print("JSON data imported successfully.")
    except Exception as e:
        print(f"Error importing JSON data: {e}")
        return

    # Initialize the object mapper
    object_mapper = ObjectMapper()

    # Map the imported data to a Python object
    try:
        data_object = object_mapper.map_to_object(data_dict, YourDataModel)
        print("Data mapped to object successfully.")
        print(data_object)
    except Exception as e:
        print(f"Error mapping data to object: {e}")

if __name__ == "__main__":
    main()