from flask import Flask, request, jsonify
from services.webhook_handler import WebhookHandler

app = Flask(__name__)
webhook_handler = WebhookHandler()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    url = data.get('url')
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    try:
        response = webhook_handler.handle_webhook(url)
        return jsonify({'status': 'success', 'response': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)