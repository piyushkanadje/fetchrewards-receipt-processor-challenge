import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
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

    
    # Register Blueprints
    app.register_blueprint(receipt_processor_api)

    return app

app = create_app()
CORS(app)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the app with configurable host and port
    app.run(
        host=os.getenv('FLASK_RUN_HOST', '0.0.0.0'),
        port=int(os.getenv('FLASK_RUN_PORT', '5000')),
        debug=app.config['DEBUG']
    )
