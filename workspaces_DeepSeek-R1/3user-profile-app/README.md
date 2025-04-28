# User Profile Application

This is a simple Flask application that allows users to create and update their profiles. User data, including names and bios, is stored in an SQLite database.

## Project Structure

```
user-profile-app
├── app.py                # Entry point of the application
├── templates             # HTML templates for the application
│   ├── base.html        # Base template with common elements
│   └── profile.html     # Template for displaying and updating user profiles
├── static               # Static files such as CSS
│   └── style.css        # Styles for the application
├── database             # Database files
│   └── user_profiles.db # SQLite database for storing user profiles
├── models.py            # Data model for user profiles
├── requirements.txt     # List of dependencies
└── README.md            # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd user-profile-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your web browser and navigate to `http://127.0.0.1:5000` to access the application.

## Usage

- Users can view their profile and update their name and bio through the provided form.
- The application connects to an SQLite database to store and retrieve user profile information.

## License

This project is licensed under the MIT License.