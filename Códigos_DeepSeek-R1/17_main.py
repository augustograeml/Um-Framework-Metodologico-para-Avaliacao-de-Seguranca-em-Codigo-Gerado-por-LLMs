import json
import os
from utils.script_runner import ScriptRunner

def load_config(config_path):
    with open(config_path, 'r') as config_file:
        return json.load(config_file)

def main():
    config = load_config('config/config.json')
    script_runner = ScriptRunner()

    # Example: Load and execute a user-defined script
    user_script_path = 'src/scripts/user_scripts/example_script.py'  # Replace with actual user script path
    if script_runner.validate_script(user_script_path):
        script_runner.run_script(user_script_path)
    else:
        print("Script validation failed.")

if __name__ == "__main__":
    main()