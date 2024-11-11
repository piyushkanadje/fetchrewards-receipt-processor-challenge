from flask import  Blueprint
import logging
# Configure the logger
logger = logging.getLogger(__name__)
receipt_processor_api = Blueprint('receipt_processor', __name__, url_prefix="/receipts")
from . import routes

