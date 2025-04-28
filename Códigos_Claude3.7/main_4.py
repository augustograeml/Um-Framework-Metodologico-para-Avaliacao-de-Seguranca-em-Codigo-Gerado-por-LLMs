from flask import Flask, request, jsonify
from app.database.connection import get_db_connection
from app.search.query import search_users
from app.utils.validators import validate_search_input

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    name = request.args.get('name', '')
    email = request.args.get('email', '')

    if not validate_search_input(name, email):
        return jsonify({'error': 'Invalid input'}), 400

    with get_db_connection() as conn:
        results = search_users(conn, name, email)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)