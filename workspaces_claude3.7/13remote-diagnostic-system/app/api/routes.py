from flask import Blueprint, request, jsonify
from app.commands.executor import CommandExecutor

api_bp = Blueprint('api', __name__)
executor = CommandExecutor()

@api_bp.route('/execute', methods=['POST'])
def execute_command():
    data = request.get_json()
    command = data.get('command')

    if not command:
        return jsonify({'error': 'No command provided'}), 400

    try:
        output = executor.run(command)
        return jsonify({'output': output}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200