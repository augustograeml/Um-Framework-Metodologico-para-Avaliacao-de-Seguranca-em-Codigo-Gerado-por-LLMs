from flask import Flask
from app.routes.download import download_file

app = Flask(__name__)

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    return download_file(filename)

if __name__ == '__main__':
    app.run(debug=True)