# Fund Transfer App

## Overview
The Fund Transfer App is a simple web application that simulates fund transfers between bank accounts. Users can transfer money to other users by providing the destination user ID and the amount to be transferred, ensuring that the logged-in user has sufficient balance.

## Features
- User authentication and session management
- Fund transfer functionality
- Balance validation before transfers
- Simple and intuitive user interface

## Project Structure
```
fund-transfer-app
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── services.py
│   └── templates
│       └── index.html
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd fund-transfer-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the application settings in `config.py` as needed.

## Usage
1. Run the application:
   ```
   python run.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Log in with your user credentials.

4. Use the main page to input the destination user ID and the amount you wish to transfer.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.