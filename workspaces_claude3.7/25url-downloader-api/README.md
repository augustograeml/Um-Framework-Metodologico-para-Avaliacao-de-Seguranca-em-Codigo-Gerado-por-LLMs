# URL Downloader API

This project provides an API that allows users to download content from provided URLs directly to the server. It is built using FastAPI and is designed to be simple and efficient.

## Features

- Accepts a URL from the user and downloads the content to the server.
- Handles various content types and stores them appropriately.
- Provides a clean and easy-to-use API interface.

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

4. Set up environment variables by copying the `.env.example` to `.env` and modifying it as needed.

## Usage

To run the application, execute the following command:
```
uvicorn app.main:app --reload
```

Once the server is running, you can access the API at `http://localhost:8000`.

### API Endpoints

- **POST /download**
  - Request Body: 
    ```json
    {
      "url": "http://example.com/resource"
    }
    ```
  - Response: 
    - Success: Returns the path to the downloaded file.
    - Error: Returns an error message if the download fails.

## Testing

To run the tests, use the following command:
```
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.