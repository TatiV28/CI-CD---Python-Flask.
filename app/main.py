from flask import Flask, jsonify
import os
import logging

app = Flask(__name__)

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def hello():
    return jsonify({
        'message': 'Hello from CI/CD App!',
        'version': os.getenv('APP_VERSION', '1.0.0'),
        'environment': os.getenv('ENVIRONMENT', 'development')
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

@app.route('/api/users')
def get_users():
    # Пример API эндпоинта
    users = [
        {'id': 1, 'name': 'John Doe'},
        {'id': 2, 'name': 'Jane Smith'}
    ]
    return jsonify(users)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
