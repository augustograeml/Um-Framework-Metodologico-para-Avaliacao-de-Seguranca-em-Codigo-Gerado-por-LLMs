import sys
from engine.script_executor import ScriptExecutor
from engine.sandbox import Sandbox
from config.settings import SCRIPT_TIMEOUT, MAX_SCRIPT_SIZE

def main():
    executor = ScriptExecutor()
    sandbox = Sandbox()

    print("Welcome to the Task Automation System!")
    while True:
        print("\nOptions:")
        print("1. List available scripts")
        print("2. Execute a script")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            scripts = executor.list_available_scripts()
            print("Available scripts:")
            for script in scripts:
                print(f"- {script}")

        elif choice == '2':
            script_name = input("Enter the name of the script to execute: ")
            try:
                sandbox.run_script(script_name)
            except Exception as e:
                print(f"Error executing script: {e}")

        elif choice == '3':
            print("Exiting the application.")
            sys.exit(0)

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()