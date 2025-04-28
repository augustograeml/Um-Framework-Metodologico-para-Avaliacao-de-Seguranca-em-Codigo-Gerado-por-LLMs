# User Profile Application

This project is a simple web application that allows users to create and update their profiles. The application is built using Flask and stores user data in an SQLite database.

## Features

- User can create a profile with a name and bio.
- Users can update their profile information.
- Data is stored in an SQLite database.

## Project Structure

```
user-profile-app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── forms.py
│   ├── templates
│   │   ├── base.html
│   │   ├── profile.html
│   │   └── update_profile.html
│   └── static
│       └── styles.css
├── database
│   └── user_profiles.db
├── requirements.txt
└── README.md
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
   python app/main.py
   ```

4. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Usage

- To create a new profile, navigate to the profile creation page.
- To update an existing profile, fill out the update form with the new name and bio.

## License

This project is licensed under the MIT License.