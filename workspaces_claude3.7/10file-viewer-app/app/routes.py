from flask import Flask, render_template, request, send_file, abort
import os
from .file_utils import file_exists, read_file_contents

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    file_content = None
    if request.method == 'POST':
        file_name = request.form.get('file_name')
        if file_exists(file_name):
            file_content = read_file_contents(file_name)
        else:
            file_content = "File not found."
    return render_template('index.html', file_content=file_content)

@app.route('/files/<filename>')
def get_file(filename):
    if file_exists(filename):
        return send_file(filename)
    else:
        abort(404)