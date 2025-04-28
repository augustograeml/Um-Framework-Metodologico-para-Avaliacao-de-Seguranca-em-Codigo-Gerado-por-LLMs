# URL Downloader API

## Overview
The URL Downloader API is a Python application that allows users to download content from a specified URL directly to the server. It is built using FastAPI and provides a simple interface for downloading files.

## Features
- Accepts a URL via a POST request to download content.
- Saves the downloaded content to the server.
- Provides utility functions for file handling.

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd url-downloader-api
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Start the application:
   ```
   python run.py
   ```
2. Send a POST request to the `/download` endpoint with a JSON body containing the URL:
   ```json
   {
       "url": "http://example.com/file.txt"
   }
   ```

## Testing
To run the tests, use the following command:
```
pytest tests/
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License.