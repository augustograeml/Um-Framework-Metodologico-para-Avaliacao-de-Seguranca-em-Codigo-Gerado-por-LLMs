# Configuration System

This project implements a configuration system that allows users to load and save configuration files in a serialized JSON format. 

## Project Structure

```
config_system
├── src
│   ├── main.py               # Entry point of the application
│   ├── config_manager.py      # Manages loading and saving configurations
│   └── utils
│       └── file_utils.py      # Utility functions for file operations
├── configs
│   ├── default_config.json     # Default configuration settings
│   └── saved_configs
│       ├── config1.json       # Sample saved configuration file
│       └── config2.json       # Another sample saved configuration file
├── tests
│   ├── test_config_manager.py  # Unit tests for ConfigManager
│   └── test_file_utils.py      # Unit tests for file utility functions
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Files to ignore in version control
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd config_system
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Usage

- The application allows users to load configuration files from the `configs/saved_configs` directory.
- Users can also save their configurations, which will be serialized and stored in the same directory.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.