# Python Web Application for File Downloads

This project is a simple Python web application built using Flask that allows users to download reports by providing the file name.

## Project Structure

```
python-web-app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── routes
│   │   └── download.py
│   ├── services
│   │   └── file_service.py
│   ├── templates
│   │   └── index.html
│   └── static
│       └── reports
│           └── sample_report.txt
├── requirements.txt
├── .env
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

4. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   Create a `.env` file in the root directory and add your configuration variables.

## Usage

1. **Run the application:**
   ```
   python app/main.py
   ```

2. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

3. **Download a report:**
   Enter the name of the report you wish to download in the provided input field and submit the form.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.