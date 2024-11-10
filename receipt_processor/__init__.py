from flask import  Blueprint

receipt_processor = Blueprint('receipt_processor', __name__, url_prefix="/receipts")

from . import routes

