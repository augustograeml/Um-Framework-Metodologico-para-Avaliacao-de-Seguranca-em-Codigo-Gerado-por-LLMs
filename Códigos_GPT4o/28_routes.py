from flask import Blueprint, request, jsonify
from app.auth.models import User
from app.auth.utils import hash_password, generate_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    hashed_password = hash_password(password)
    new_user = User(username=username, password_hash=hashed_password)

    # Here you would typically add the user to the database
    # db.session.add(new_user)
    # db.session.commit()

    return jsonify({'message': 'User registered successfully.'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    # Here you would typically query the user from the database
    # user = User.query.filter_by(username=username).first()

    # if user and user.verify_password(password):
    #     token = generate_token(user.id)
    #     return jsonify({'token': token}), 200

    return jsonify({'message': 'Invalid username or password.'}), 401