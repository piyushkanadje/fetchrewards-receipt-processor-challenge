import os
import logging
from flask import Flask, request, jsonify
from receipt_processor import receipt_processor_api

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)

    # Load environment-specific configurations
    app.config['DEBUG'] = os.getenv('FLASK_DEBUG', 'False') == 'True'
    app.config['ENV'] = os.getenv('FLASK_ENV', 'production')
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['PREFERRED_URL_SCHEME'] = 'https'

    # Register Blueprints
    app.register_blueprint(receipt_processor_api)

    # Global error handler
    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        logger.exception("An unexpected error occurred")
        return jsonify({"error": "An unexpected error occurred"}), 500

    return app

app = create_app()

if __name__ == '__main__':
    # Run the app with configurable host and port
    app.run(
        host=os.getenv('FLASK_RUN_HOST', '0.0.0.0'),
        port=int(os.getenv('FLASK_RUN_PORT', '5000')),
        debug=app.config['DEBUG']
    )
