from flask import Blueprint, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from app.config import Config

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(Config.UPLOAD_FOLDER, filename))
            flash('File successfully uploaded')
            return redirect(url_for('upload.upload_file'))
    return render_template('upload.html')