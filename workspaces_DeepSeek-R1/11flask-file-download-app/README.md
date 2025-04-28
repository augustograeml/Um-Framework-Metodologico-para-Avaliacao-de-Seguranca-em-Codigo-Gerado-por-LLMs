# Flask File Download Application

This project is a simple Flask web application that allows users to download reports by providing the file name. 

## Project Structure

```
flask-file-download-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   └── templates
│       └── index.html
├── reports
│   └── (report files such as report1.pdf, report2.pdf, etc.)
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-file-download-app
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

5. **Run the application:**
   ```
   python run.py
   ```

## Usage

- Open your web browser and go to `http://127.0.0.1:5000`.
- Enter the name of the report file you wish to download (e.g., `report1.pdf`) and click the download button.

## Notes

- Ensure that the report files are placed in the `reports` directory.
- The application currently supports PDF files for download. Adjust the configuration in `config.py` if you need to support other file types.