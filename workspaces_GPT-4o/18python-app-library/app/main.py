import importlib
import os

def main():
    print("Welcome to the dynamic library loader application!")

    # Example of loading a user-provided library
    library_name = input("Enter the name of the library to load: ")
    loader = DynamicLoader()
    try:
        loader.load_library(library_name)
        print(f"Library '{library_name}' loaded successfully.")
    except Exception as e:
        print(f"Error loading library '{library_name}': {e}")

    # Additional application logic can go here

if __name__ == "__main__":
    main()