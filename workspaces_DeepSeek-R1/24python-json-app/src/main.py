def main():
    import os
    from utils.json_importer import import_json
    from models.data_model import DataModel

    print("Welcome to the JSON Importer Application!")
    
    file_path = input("Please enter the path to the JSON file you want to import: ")
    
    if not os.path.exists(file_path):
        print("The specified file does not exist. Please check the path and try again.")
        return

    try:
        json_data = import_json(file_path)
        data_model = DataModel(**json_data)
        print("Data imported successfully!")
        print(data_model)
    except Exception as e:
        print(f"An error occurred while importing the JSON data: {e}")

if __name__ == "__main__":
    main()