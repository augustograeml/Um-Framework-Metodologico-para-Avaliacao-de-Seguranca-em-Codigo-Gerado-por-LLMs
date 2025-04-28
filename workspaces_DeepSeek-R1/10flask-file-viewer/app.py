from flask import Flask, render_template, request, send_from_directory, abort
import os

app = Flask(__name__)

# Path to the directory where files are stored
FILES_DIRECTORY = 'files'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view-file', methods=['POST'])
def view_file():
    file_name = request.form.get('file_name')
    if file_name:
        file_path = os.path.join(FILES_DIRECTORY, file_name)
        if os.path.isfile(file_path):
            return send_from_directory(FILES_DIRECTORY, file_name)
        else:
            return "File not found", 404
    return "No file name provided", 400

if __name__ == '__main__':
    app.run(debug=True)