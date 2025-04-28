# Webhook Service

This project implements a webhook service that accepts URLs sent by users and makes HTTP requests to those addresses.

## Project Structure

```
webhook-service
├── src
│   ├── app.py                # Entry point of the application
│   ├── services
│   │   └── webhook_handler.py # Handles incoming webhook requests
│   ├── utils
│   │   └── http_client.py     # Utility for making HTTP requests
│   └── tests
│       ├── test_app.py       # Unit tests for the app
│       └── test_webhook_handler.py # Unit tests for the WebhookHandler class
├── requirements.txt           # Project dependencies
├── .env                       # Environment variables
├── .gitignore                 # Files to ignore in Git
└── README.md                  # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd webhook-service
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
python src/app.py
```

The application will start and listen for incoming webhook requests.

## Testing

To run the tests, use:
```
pytest src/tests
```

This will execute all unit tests and provide feedback on the functionality of the application.