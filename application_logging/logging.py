import logging
from functools import wraps
from flask import request, jsonify
from pydantic import ValidationError

# Configure the logger
logger = logging.getLogger(__name__)

def log_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # Log the incoming request data
            data = request.get_json()
            logger.info(f"Processing request with data: {data}")
            
            # Pass the data along to the wrapped function
            return func(*args, **kwargs)

        except ValidationError as e:
            # Log and return validation errors
            error_details = [
                {"field": err["loc"][0] if "loc" in err and err["loc"] else "unknown_field", "message": err["msg"]}
                for err in e.errors()
            ]
            logger.warning(f"Validation error(s): {error_details}")
            return jsonify({"error": error_details}), 400

        except Exception as e:
            # Log unexpected exceptions
            logger.exception("Unexpected error during request processing")
            return jsonify({"status": "error", "message": "Internal server error"}), 500

    return wrapper
