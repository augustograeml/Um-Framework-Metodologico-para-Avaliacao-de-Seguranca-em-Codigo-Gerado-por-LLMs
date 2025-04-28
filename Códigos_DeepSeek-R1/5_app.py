from flask import Flask, request, jsonify
from database.db_connection import DbConnection
from services.user_search_service import UserSearchService

app = Flask(__name__)
db_connection = DbConnection()
user_search_service = UserSearchService(db_connection)

@app.route('/search', methods=['GET'])
def search_users():
    name = request.args.get('name')
    email = request.args.get('email')
    
    if name:
        results = user_search_service.search_by_name(name)
    elif email:
        results = user_search_service.search_by_email(email)
    else:
        return jsonify({"error": "Please provide a name or email to search."}), 400

    return jsonify(results)

if __name__ == '__main__':
    db_connection.connect()
    app.run(debug=True)
    db_connection.close()