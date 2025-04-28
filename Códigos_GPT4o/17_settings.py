# Configuration settings for the Python automation application

class Config:
    SCRIPT_EXECUTION_PERMISSIONS = {
        'allow': ['*.py'],  # Allow execution of Python scripts
        'deny': ['*.sh', '*.bat']  # Deny execution of shell and batch scripts
    }
    
    LOGGING_SETTINGS = {
        'level': 'INFO',  # Set the logging level
        'format': '%(asctime)s - %(levelname)s - %(message)s',  # Log message format
        'file': 'app.log'  # Log file name
    }