from flask import Flask, send_from_directory, request, render_template, abort
import os

app = Flask(__name__)

# Configuration
app.config['REPORTS_FOLDER'] = os.path.join(os.getcwd(), 'reports')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        return send_from_directory(app.config['REPORTS_FOLDER'], filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)