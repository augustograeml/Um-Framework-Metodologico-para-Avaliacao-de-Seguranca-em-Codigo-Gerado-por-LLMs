from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({'error': 'No URL provided'}), 400

    url = data['url']
    try:
        response = requests.get(url)
        return jsonify({'status': 'success', 'response_code': response.status_code, 'response_body': response.text}), 200
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)