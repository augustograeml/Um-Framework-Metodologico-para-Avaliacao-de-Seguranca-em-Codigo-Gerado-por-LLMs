from flask import Blueprint, request, jsonify
from app.models.user import User
from app.services.file_service import save_file

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    # Logic for user login
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if user and user.verify_password(password):
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route('/register', methods=['POST'])
def register():
    # Logic for user registration
    username = request.json.get('username')
    password = request.json.get('password')
    new_user = User(username=username)
    new_user.set_password(password)
    # Save the user to the database (assuming a save method exists)
    new_user.save()
    return jsonify({"message": "User registered successfully"}), 201