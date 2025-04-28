# Python Web Application for File Uploads

This project is a simple web application built using Flask that allows users to upload documents to the server. The application includes file upload functionality, form validation, and a user-friendly interface.

## Project Structure

```
python-web-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── forms.py
│   ├── templates
│   │   ├── base.html
│   │   ├── upload.html
│   │   └── success.html
│   └── static
│       └── uploads
├── instance
│   └── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd python-web-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

5. **Configure the application:**
   Update the `instance/config.py` file with your desired settings, such as the upload folder and allowed file types.

6. **Run the application:**
   ```
   python run.py
   ```

7. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000/upload` to access the file upload form.

## Usage

- Navigate to the upload page to select and upload your documents.
- After a successful upload, you will be redirected to a success page confirming the upload.

## License

This project is licensed under the MIT License.