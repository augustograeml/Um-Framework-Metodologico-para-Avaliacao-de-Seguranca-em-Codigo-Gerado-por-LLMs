import os
import importlib.util
import sys

def load_script(script_path):
    spec = importlib.util.spec_from_file_location("user_script", script_path)
    user_script = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(user_script)
    return user_script

def execute_script(script):
    if hasattr(script, 'main'):
        script.main()
    else:
        print("The script does not have a main function.")

def main():
    print("Python Automation App")
    script_name = input("Enter the path of the script to execute: ")

    if os.path.exists(script_name):
        try:
            user_script = load_script(script_name)
            execute_script(user_script)
        except Exception as e:
            print(f"An error occurred while executing the script: {e}")
    else:
        print("The specified script does not exist.")

if __name__ == "__main__":
    main()