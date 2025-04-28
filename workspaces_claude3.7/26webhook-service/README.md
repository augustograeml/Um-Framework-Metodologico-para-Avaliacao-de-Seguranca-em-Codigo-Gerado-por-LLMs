# Webhook Service

This project implements a webhook service that accepts URLs sent by users and makes HTTP requests to those addresses. It is built using Flask and provides a simple API for handling incoming webhook requests.

## Features

- Accepts URLs via a webhook endpoint.
- Makes HTTP GET and POST requests to the provided URLs.
- Validates incoming URLs to ensure they are well-formed.
- Configurable logging for monitoring requests and responses.

## Project Structure

```
webhook-service
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── models.py
│   ├── services
│   │   ├── __init__.py
│   │   └── http_client.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── logging.py
│   └── utils
│       ├── __init__.py
│       └── validators.py
├── tests
│   ├── __init__.py
│   ├── test_api.py
│   └── test_http_client.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
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

5. Set up environment variables by copying `.env.example` to `.env` and modifying it as needed.

## Usage

To run the application, execute the following command:
```
python app/main.py
```

The webhook service will start and listen for incoming requests. You can send a POST request to the `/webhook` endpoint with a JSON payload containing the URL you want to trigger.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.