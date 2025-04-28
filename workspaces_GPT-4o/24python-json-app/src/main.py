import json
import os
from services.json_importer import JsonImporter

def main():
    print("Welcome to the JSON Importer App!")
    file_path = input("Please enter the path to the JSON file you want to import: ")

    if not os.path.isfile(file_path):
        print("The specified file does not exist. Please try again.")
        return

    importer = JsonImporter()
    try:
        data = importer.import_json(file_path)
        print("Data imported successfully:")
        print(data)
    except Exception as e:
        print(f"An error occurred while importing JSON: {e}")

if __name__ == "__main__":
    main()