# Bank Transfer App

This project simulates a simplified fund transfer functionality between bank accounts. Users can transfer funds to other accounts while ensuring they have sufficient balance.

## Features

- User authentication (login/logout)
- Fund transfer between accounts
- Balance validation before transfers
- User dashboard to view account details

## Project Structure

```
bank-transfer-app
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── account.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── transfers.py
│   ├── services
│   │   ├── __init__.py
│   │   └── transfer_service.py
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   └── js
│   │       └── main.js
│   └── templates
│       ├── base.html
│       ├── login.html
│       ├── dashboard.html
│       └── transfer.html
├── tests
│   ├── __init__.py
│   ├── test_models.py
│   └── test_transfers.py
├── venv
├── .env
├── .gitignore
├── requirements.txt
├── run.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd bank-transfer-app
   ```
3. Create a virtual environment:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Set up your environment variables in the `.env` file.
2. Run the application:
   ```
   python run.py
   ```
3. Access the application in your web browser at `http://localhost:5000`.

## Testing

To run the tests, ensure your virtual environment is activated and execute:
```
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.