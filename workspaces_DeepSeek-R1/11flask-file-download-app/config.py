import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    REPORTS_FOLDER = os.path.join(os.getcwd(), 'reports')
    ALLOWED_EXTENSIONS = {'pdf', 'docx', 'xlsx'}  # Add other allowed file types as needed

    @staticmethod
    def is_allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS