# Python Backup Application

This project provides a simple backup module for saving and restoring Python objects to and from files. It includes functionality to serialize Python objects and store them in a file, as well as to retrieve them when needed.

## Features

- Save Python objects to a file.
- Load Python objects from a file.
- Easy-to-use interface for backing up and restoring data.

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

### Saving an Object

To save a Python object, you can use the `BackupSaver` class from the `backup.save` module:

```python
from backup.save import BackupSaver

saver = BackupSaver()
my_object = {'key': 'value'}
saver.save(my_object, 'my_object_backup.pkl')
```

### Restoring an Object

To restore a Python object, use the `BackupRestorer` class from the `backup.restore` module:

```python
from backup.restore import BackupRestorer

restorer = BackupRestorer()
restored_object = restorer.restore('my_object_backup.pkl')
print(restored_object)
```

## Running Tests

To run the tests for this project, navigate to the `tests` directory and run:

```
python -m unittest discover
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or bugs.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.