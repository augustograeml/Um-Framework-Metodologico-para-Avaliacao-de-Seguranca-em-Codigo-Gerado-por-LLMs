from flask import Blueprint, request, jsonify
from app.services.http_client import HttpClient
from app.utils.validators import is_valid_url

api_bp = Blueprint('api', __name__)
http_client = HttpClient()

@api_bp.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    url = data.get('url')

    if not url or not is_valid_url(url):
        return jsonify({'error': 'Invalid URL'}), 400

    response = http_client.get(url)
    return jsonify({'status': 'success', 'response': response}), 200

def register_routes(app):
    app.register_blueprint(api_bp)