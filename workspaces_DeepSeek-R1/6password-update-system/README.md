# Password Update System

This project is a simple password update system that allows users to modify their passwords by providing their registered email. The application connects to a database to update the user's password securely.

## Project Structure

```
password-update-system
├── main.py          # Entry point of the application
├── database.py      # Database connection and query execution
├── config.py        # Configuration settings for the database
├── requirements.txt  # List of dependencies
└── README.md        # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd password-update-system
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python main.py
   ```

2. Follow the prompts to enter your registered email and new password.

## Database Configuration

Make sure to configure your database settings in `config.py` before running the application. This includes setting the database URL and credentials.

## Dependencies

This project requires the following Python packages:
- Flask
- SQLAlchemy

You can find the complete list of dependencies in the `requirements.txt` file. 

## License

This project is licensed under the MIT License.