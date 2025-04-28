# Python Backup Application

This project implements a backup module that allows users to save and restore Python objects to and from files. It provides a simple command-line interface for managing backups.

## Project Structure

```
python-backup-app
├── src
│   ├── backup_module
│   │   ├── __init__.py
│   │   ├── backup.py
│   │   └── restore.py
│   └── main.py
├── tests
│   ├── __init__.py
│   └── test_backup_module
│       ├── __init__.py
│       ├── test_backup.py
│       └── test_restore.py
├── data
│   └── backups
├── requirements.txt
├── README.md
└── .gitignore
```

## Features

- **BackupManager**: A class responsible for saving Python objects to files and listing available backups.
- **RestoreManager**: A class responsible for restoring Python objects from backup files and listing restored objects.

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To use the application, run the following command:

```
python src/main.py
```

Follow the prompts to save or restore Python objects.

## Testing

To run the tests for the backup and restore functionality, navigate to the `tests` directory and run:

```
pytest
```

## License

This project is licensed under the MIT License.