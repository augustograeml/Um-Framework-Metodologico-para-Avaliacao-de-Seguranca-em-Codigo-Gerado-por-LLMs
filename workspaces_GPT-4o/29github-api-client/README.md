# GitHub API Client

This project is a Python application that implements a client to consume the GitHub API. It allows users to authenticate using a Personal Access Token (PAT) and retrieve information about a specific user's repositories.

## Features

- Authenticate with GitHub using a Personal Access Token.
- Retrieve a list of repositories for a specified user.
- Handle API responses and errors gracefully.

## Requirements

- Python 3.x
- Requests library

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd github-api-client
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Personal Access Token (PAT):
   - Create a `.env` file in the root directory and add your PAT:
     ```
     GITHUB_TOKEN=your_personal_access_token
     ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

You will be prompted to enter a GitHub username, and the application will display the repositories associated with that user.

## Testing

To run the unit tests, use the following command:
```
pytest tests/
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.