from flask import Flask, render_template, request
from services.log_analysis import LogAnalyzer

app = Flask(__name__)
log_analyzer = LogAnalyzer()

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        results = log_analyzer.search_logs(search_term)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)