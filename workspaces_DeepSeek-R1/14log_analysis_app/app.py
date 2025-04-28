from flask import Flask, render_template, request
import re

app = Flask(__name__)

def search_logs(term):
    results = []
    with open('logs/sample.log', 'r') as log_file:
        for line in log_file:
            if re.search(term, line, re.IGNORECASE):
                results.append(line.strip())
    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        search_term = request.form['search_term']
        results = search_logs(search_term)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)