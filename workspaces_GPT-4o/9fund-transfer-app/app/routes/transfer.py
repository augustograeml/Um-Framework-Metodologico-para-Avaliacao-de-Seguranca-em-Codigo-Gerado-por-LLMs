from flask import Blueprint, request, jsonify
from app.services.transfer_service import TransferService
from app.utils.validation import validate_transfer_input

transfer_bp = Blueprint('transfer', __name__)
transfer_service = TransferService()

@transfer_bp.route('/transfer', methods=['POST'])
def transfer():
    data = request.get_json()
    user_id = request.user_id  # Assuming user_id is set in the request context after authentication
    amount = data.get('amount')
    destination_user_id = data.get('destination_user_id')

    # Validate input
    validation_error = validate_transfer_input(amount, destination_user_id)
    if validation_error:
        return jsonify({'error': validation_error}), 400

    # Perform transfer
    success, message = transfer_service.transfer_funds(user_id, destination_user_id, amount)
    if success:
        return jsonify({'message': message}), 200
    else:
        return jsonify({'error': message}), 400