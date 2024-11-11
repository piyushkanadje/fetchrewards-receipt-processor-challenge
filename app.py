
from flask import Flask, request
from receipt_processor import receipt_processor_api
import logging

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()  # StreamHandler outputs logs to the console
    ]
)

app = Flask(__name__)
@app.route('/')
def home():
    return "Hello World!"

app.register_blueprint(receipt_processor_api)


if __name__ == '__main__':
    app.run(debug=True)