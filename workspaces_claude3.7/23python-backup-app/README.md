# Python Backup Application

This project implements a backup module for saving and restoring Python objects to and from files. It provides a simple command-line interface for users to interact with the backup functionality.

## Features

- Serialize and save Python objects to files.
- Restore Python objects from serialized files.
- Easy-to-use command-line interface.

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To save a Python object, use the `save_object` function from the `backup.save` module:

```python
from src.backup.save import save_object

my_object = {'key': 'value'}
save_object(my_object, 'my_object.pkl')
```

To restore a Python object, use the `restore_object` function from the `backup.restore` module:

```python
from src.backup.restore import restore_object

my_object = restore_object('my_object.pkl')
print(my_object)  # Output: {'key': 'value'}
```

## Running Tests

To run the unit tests for the backup module, execute:

```
pytest tests/
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.