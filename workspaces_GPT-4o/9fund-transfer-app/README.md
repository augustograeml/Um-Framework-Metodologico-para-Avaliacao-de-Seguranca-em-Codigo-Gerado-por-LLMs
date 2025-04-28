# Fund Transfer Application

This is a simplified fund transfer application built with Python and Flask. It allows users to transfer funds between bank accounts while ensuring that the sender has sufficient balance.

## Project Structure

```
fund-transfer-app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   │   └── account.py
│   ├── routes
│   │   └── transfer.py
│   ├── services
│   │   └── transfer_service.py
│   └── utils
│       └── validation.py
├── tests
│   ├── __init__.py
│   ├── test_transfer.py
│   └── test_validation.py
├── requirements.txt
├── .env
└── README.md
```

## Features

- User authentication (not implemented in this version)
- Fund transfer between accounts
- Input validation for transfer requests
- Unit tests for transfer functionality and validation

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fund-transfer-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up environment variables in the `.env` file as needed.

## Usage

To run the application, execute the following command:
```
python app/main.py
```

You can then use tools like Postman or curl to send POST requests to the transfer endpoint to initiate fund transfers.

## Running Tests

To run the tests, ensure your virtual environment is activated and execute:
```
pytest
```

## License

This project is licensed under the MIT License.