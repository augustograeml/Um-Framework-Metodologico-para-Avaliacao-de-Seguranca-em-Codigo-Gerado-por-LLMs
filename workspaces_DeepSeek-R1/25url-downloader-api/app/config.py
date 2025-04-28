import os

class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DOWNLOAD_FOLDER = os.path.join(BASE_DIR, 'downloads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB limit
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip', 'tar', 'gz'}

    @staticmethod
    def is_allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS