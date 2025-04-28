# GitHub API Client

This project is a Python application that interacts with the GitHub API to retrieve information about a specific user's repositories using a Personal Access Token (PAT) for authentication.

## Features

- Authenticate with GitHub API using a Personal Access Token.
- Retrieve a list of repositories for a specified GitHub user.
- Simple command-line interface for user interaction.

## Requirements

- Python 3.6 or higher
- Required Python packages listed in `requirements.txt`

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd github-api-client
   ```

2. **Create a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up your Personal Access Token:**
   - Copy `.env.example` to `.env` and add your GitHub PAT:
     ```
     GITHUB_TOKEN=your_personal_access_token
     ```

## Usage

To run the application, execute the following command:

```
python src/main.py
```

Follow the prompts to enter the GitHub username for which you want to retrieve repositories.

## Testing

To run the tests, use the following command:

```
pytest
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.