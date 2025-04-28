# Flask Blog Application

This is a simple Flask blog application that allows users to post comments on blog posts. The application is structured to separate concerns and make it easy to manage and extend.

## Project Structure

```
flask-blog
├── app
│   ├── __init__.py          # Initializes the Flask application
│   ├── config.py            # Configuration settings for the application
│   ├── models                # Contains database models
│   │   ├── __init__.py
│   │   ├── comment.py        # Defines the Comment model
│   │   └── post.py           # Defines the Post model
│   ├── routes                # Contains route definitions
│   │   ├── __init__.py
│   │   ├── auth.py           # Handles authentication routes
│   │   ├── blog.py           # Manages blog post routes
│   │   └── comments.py       # Manages comment routes
│   ├── forms                 # Contains form definitions
│   │   ├── __init__.py
│   │   └── comment_form.py    # Defines the CommentForm class
│   ├── static                # Contains static files (CSS, JS)
│   │   ├── css
│   │   │   └── style.css
│   │   └── js
│   │       └── main.js
│   └── templates             # Contains HTML templates
│       ├── base.html
│       ├── blog
│       │   ├── index.html    # Displays list of blog posts
│       │   └── post.html     # Displays a single blog post
│       └── partials
│           └── comment_form.html # Contains the comment form HTML
├── migrations                # Database migrations
│   └── README.md
├── .env.example              # Example environment variables
├── .gitignore                # Files to ignore by Git
├── config.py                 # Additional configuration settings
├── requirements.txt          # Project dependencies
├── run.py                    # Entry point to run the application
└── README.md                 # Project documentation
```

## Features

- Users can view blog posts and their associated comments.
- Users can submit comments on blog posts.
- The application is built using Flask and follows a modular structure.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-blog
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the environment variables by copying `.env.example` to `.env` and updating the values as needed.

5. Run the application:
   ```
   python run.py
   ```

## Usage

- Access the application in your web browser at `http://127.0.0.1:5000`.
- Navigate through the blog posts and submit comments as desired.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.