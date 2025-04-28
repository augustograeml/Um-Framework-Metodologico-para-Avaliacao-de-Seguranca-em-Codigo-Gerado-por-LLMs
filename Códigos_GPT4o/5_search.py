from flask import Blueprint, request, render_template
from app.services.search_service import SearchService

search_bp = Blueprint('search', __name__)
search_service = SearchService()

@search_bp.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get('query', '')
    results = []
    
    if query:
        results = search_service.search_users(query)

    return render_template('search.html', results=results)