# Task Automation System

## Overview
The Task Automation System is a Python application designed to allow users to execute custom scripts for automating various system tasks. It provides a secure environment for running scripts, along with a set of example scripts to help users get started.

## Features
- Execute user-provided scripts with the `ScriptExecutor` class.
- A secure execution environment provided by the `Sandbox` class.
- Example scripts for common tasks such as file operations and retrieving system information.
- Configuration settings to customize script execution behavior.

## Getting Started
To get started with the Task Automation System, follow these steps:

1. **Clone the Repository**
   ```
   git clone <repository-url>
   cd task-automation-system
   ```

2. **Install Dependencies**
   Make sure you have Python installed, then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Application**
   You can run the application using:
   ```
   python src/main.py
   ```

## Usage
- Users can create their own scripts and place them in the `user_scripts` directory.
- The application provides a command-line interface to execute these scripts.
- Refer to the `user_scripts/README.md` for detailed instructions on creating and executing custom scripts.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.