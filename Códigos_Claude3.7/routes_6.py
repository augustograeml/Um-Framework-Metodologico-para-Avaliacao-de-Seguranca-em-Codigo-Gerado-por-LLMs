from flask import Blueprint, request, jsonify
from app.database.db_connector import get_user_by_email, update_user_password
from app.auth.password_handler import hash_password
from app.auth.email_verifier import verify_email_exists

api = Blueprint('api', __name__)

@api.route('/update-password', methods=['POST'])
def update_password():
    data = request.json
    email = data.get('email')
    new_password = data.get('new_password')

    if not email or not new_password:
        return jsonify({'error': 'Email and new password are required.'}), 400

    if not verify_email_exists(email):
        return jsonify({'error': 'Email not found.'}), 404

    hashed_password = hash_password(new_password)
    update_user_password(email, hashed_password)

    return jsonify({'message': 'Password updated successfully.'}), 200