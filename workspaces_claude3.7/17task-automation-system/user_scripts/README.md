# User Scripts for Task Automation System

Welcome to the Task Automation System! This document provides instructions on how to create and execute your custom scripts to automate system tasks.

## Creating Custom Scripts

1. **Script Structure**: Your script should be a plain text file with a `.py` extension. Ensure that it follows Python syntax and conventions.

2. **Function Definitions**: Define functions in your script that perform specific tasks. For example:
   ```python
   def my_custom_function():
       # Your code here
       pass
   ```

3. **Script Location**: Place your custom scripts in the `user_scripts` directory for easy access and execution.

## Executing Scripts

1. **Using the Script Executor**: You can execute your scripts using the `ScriptExecutor` class provided in the application. 

2. **Command Line Interface**: If the application supports a command line interface, you can run your script by executing:
   ```
   python main.py execute <script_name.py>
   ```

3. **Listing Available Scripts**: To see a list of all available scripts, you can use:
   ```
   python main.py list
   ```

## Example Scripts

Refer to the `src/scripts/examples` directory for example scripts that demonstrate various functionalities, such as file operations and system information retrieval.

## Important Notes

- Ensure that your scripts do not contain harmful commands that could affect system stability or security.
- Test your scripts in a safe environment before executing them in a production setting.

Happy scripting!