from flask import Blueprint, render_template, request
from app.log_analyzer.search import LogSearcher

web_routes = Blueprint('web_routes', __name__)

@web_routes.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@web_routes.route('/search', methods=['POST'])
def search():
    search_term = request.form.get('search_term')
    log_searcher = LogSearcher()
    results = log_searcher.search_terms(search_term)
    return render_template('results.html', results=results)