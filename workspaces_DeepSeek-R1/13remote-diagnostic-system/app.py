from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute_command():
    command = request.form.get('command')
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return jsonify({'output': output, 'error': None})
    except subprocess.CalledProcessError as e:
        return jsonify({'output': e.output, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)