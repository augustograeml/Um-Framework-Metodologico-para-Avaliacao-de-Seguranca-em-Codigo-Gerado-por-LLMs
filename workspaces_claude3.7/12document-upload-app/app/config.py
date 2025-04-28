import os

class Config:
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app', 'uploads')
    ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'txt', 'ppt', 'pptx'}

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS