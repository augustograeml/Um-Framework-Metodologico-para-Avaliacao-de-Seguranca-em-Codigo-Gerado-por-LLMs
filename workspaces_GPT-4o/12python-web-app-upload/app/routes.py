from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

app = Blueprint('app', __name__)

UPLOAD_FOLDER = 'app/static/uploads'
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return redirect(url_for('app.success'))

    flash('File type not allowed')
    return redirect(request.url)

@app.route('/success')
def success():
    return render_template('success.html')