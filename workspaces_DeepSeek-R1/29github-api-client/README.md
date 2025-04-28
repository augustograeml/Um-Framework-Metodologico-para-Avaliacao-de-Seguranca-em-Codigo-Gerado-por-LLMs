# GitHub API Client

This project is a Python application that interacts with the GitHub API to retrieve information about a specific user's repositories. It uses a Personal Access Token (PAT) for authentication to make secure API calls.

## Project Structure

```
github-api-client
├── src
│   ├── main.py            # Entry point of the application
│   ├── github_client.py    # Contains the GitHubClient class for API interactions
│   ├── config.py          # Loads configuration settings from the .env file
│   └── utils.py           # Utility functions for formatting and printing data
├── tests
│   ├── test_github_client.py  # Unit tests for the GitHubClient class
│   └── test_utils.py          # Unit tests for utility functions
├── .env                      # Environment variables, including the Personal Access Token
├── requirements.txt          # Project dependencies
├── README.md                 # Project documentation
└── .gitignore                # Files and directories to ignore by Git
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd github-api-client
   ```

2. Create a `.env` file in the root directory and add your GitHub Personal Access Token:
   ```
   GITHUB_TOKEN=your_personal_access_token
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py <github_username>
```
Replace `<github_username>` with the GitHub username whose repositories you want to retrieve.

## Testing

To run the tests, use the following command:
```
pytest
```

## License

This project is licensed under the MIT License.