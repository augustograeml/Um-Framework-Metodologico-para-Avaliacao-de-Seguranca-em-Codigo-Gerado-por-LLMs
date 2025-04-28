# main.py

from flask import Flask, request, jsonify
from database import update_password

app = Flask(__name__)

@app.route('/update-password', methods=['POST'])
def update_password_route():
    data = request.json
    email = data.get('email')
    new_password = data.get('new_password')

    if not email or not new_password:
        return jsonify({'error': 'Email and new password are required.'}), 400

    # Here you can add additional validation for email format and password strength

    success = update_password(email, new_password)
    
    if success:
        return jsonify({'message': 'Password updated successfully.'}), 200
    else:
        return jsonify({'error': 'Failed to update password. Please check the email.'}), 400

if __name__ == '__main__':
    app.run(debug=True)