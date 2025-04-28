from flask import Flask, render_template, request
from utils.file_handler import get_file_content

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    file_content = ""
    if request.method == 'POST':
        file_name = request.form.get('file_name')
        file_content = get_file_content(file_name)
    return render_template('index.html', file_content=file_content)

if __name__ == '__main__':
    app.run(debug=True)