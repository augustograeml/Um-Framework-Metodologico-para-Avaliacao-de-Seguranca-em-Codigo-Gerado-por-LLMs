from flask import Blueprint, request, jsonify, session
from .models import User
from .services import transfer_funds

bp = Blueprint('routes', __name__)

@bp.route('/transfer', methods=['POST'])
def transfer():
    data = request.get_json()
    destination_user_id = data.get('destination_user_id')
    amount = data.get('amount')

    if not destination_user_id or not amount:
        return jsonify({'error': 'Destination user ID and amount are required.'}), 400

    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'User not logged in.'}), 401

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found.'}), 404

    if transfer_funds(user, destination_user_id, amount):
        return jsonify({'message': 'Transfer successful.'}), 200
    else:
        return jsonify({'error': 'Transfer failed. Check your balance or destination user ID.'}), 400