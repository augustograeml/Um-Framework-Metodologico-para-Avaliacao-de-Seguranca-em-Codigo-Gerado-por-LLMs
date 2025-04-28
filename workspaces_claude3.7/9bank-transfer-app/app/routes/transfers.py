from flask import Blueprint, request, jsonify, session
from app.models.user import User
from app.services.transfer_service import TransferService

transfers_bp = Blueprint('transfers', __name__)

@transfers_bp.route('/transfer', methods=['POST'])
def transfer():
    data = request.get_json()
    destination_user_id = data.get('destination_user_id')
    amount = data.get('amount')

    if not destination_user_id or not amount:
        return jsonify({'error': 'Destination user ID and amount are required.'}), 400

    logged_in_user_id = session.get('user_id')
    if not logged_in_user_id:
        return jsonify({'error': 'User not logged in.'}), 401

    user = User.get_user_by_id(logged_in_user_id)
    if user.balance < amount:
        return jsonify({'error': 'Insufficient balance.'}), 400

    transfer_service = TransferService()
    success = transfer_service.execute_transfer(user, destination_user_id, amount)

    if success:
        return jsonify({'message': 'Transfer successful.'}), 200
    else:
        return jsonify({'error': 'Transfer failed.'}), 500