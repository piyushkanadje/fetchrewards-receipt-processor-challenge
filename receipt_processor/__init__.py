from flask import  Blueprint

receipt_processor_api = Blueprint('receipt_processor', __name__, url_prefix="/receipts")

from . import routes

