# User Search Application

This project implements a user search module that allows querying records in a database by name or email. The results are dynamically filtered based on user inputs.

## Project Structure

```
user-search-app
├── app.py
├── database
│   ├── __init__.py
│   └── db_connection.py
├── models
│   ├── __init__.py
│   └── user.py
├── services
│   ├── __init__.py
│   └── user_search_service.py
├── tests
│   ├── __init__.py
│   ├── test_db_connection.py
│   └── test_user_search_service.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd user-search-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the database connection in `database/db_connection.py` as needed.

## Usage

To run the application, execute the following command:
```
python app.py
```

You can then search for users by name or email through the provided interface.

## Testing

To run the tests, use:
```
pytest
```

This will execute the unit tests defined in the `tests` directory.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.