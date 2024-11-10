
from flask import Flask, render_template, request
from receipt_processor import receipt_processor_api

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

app.register_blueprint(receipt_processor_api)


if __name__ == '__main__':
    app.run(debug=True)