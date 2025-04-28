# Webhook Service

This project implements a simple webhook service using Flask that accepts URLs sent by users and makes HTTP requests to those addresses.

## Features

- Accepts incoming HTTP POST requests containing URLs.
- Makes HTTP requests to the provided URLs.
- Returns the response from the requested URL back to the user.

## Requirements

- Python 3.x
- Flask
- Requests

## Setup

1. Clone the repository:

   ```
   git clone <repository-url>
   cd webhook_service
   ```

2. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Running the Service

To run the webhook service, execute the following command:

```
python app.py
```

The service will start and listen for incoming requests on `http://127.0.0.1:5000/webhook`.

## Sending Requests

You can send a POST request to the webhook service using tools like `curl` or Postman. Here’s an example using `curl`:

```
curl -X POST http://127.0.0.1:5000/webhook -H "Content-Type: application/json" -d '{"url": "http://example.com"}'
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.