from flask import Blueprint, request, jsonify
from app.services.password_service import update_password
from app.utils.email_validator import is_valid_email

routes = Blueprint('routes', __name__)

@routes.route('/update-password', methods=['POST'])
def update_password_route():
    data = request.get_json()
    email = data.get('email')
    new_password = data.get('new_password')

    if not email or not new_password:
        return jsonify({'error': 'Email and new password are required.'}), 400

    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email format.'}), 400

    success = update_password(email, new_password)

    if success:
        return jsonify({'message': 'Password updated successfully.'}), 200
    else:
        return jsonify({'error': 'Failed to update password. Email may not be registered.'}), 404