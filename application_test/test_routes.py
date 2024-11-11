
import pytest

class TestProcessReceiptForId:

    def test_process_valid_receipt(self, mocker):
        from flask import Flask
        from receipt_processor.routes import process_receipt_for_id
        from receipt_processor.data_validation import Receipt
        import json

        app = Flask(__name__)
        app.config['TESTING'] = True

        valid_receipt_data = {
            "retailer": "M&M Corner Market",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "items": [{"name": "item1", "price": "3.00"}, {"name": "item2", "price": "3.49"}],
            "total": "6.49"
        }

        with app.test_request_context('/process', method='POST', data=json.dumps(valid_receipt_data), content_type='application/json'):
            mocker.patch('uuid.uuid4', return_value='1234')
            response = process_receipt_for_id()
            assert response.status_code == 200
            assert response.get_json() == {"id": "1234"}

    def test_empty_json_payload(self, mocker):
        from flask import Flask
        from receipt_processor.routes import process_receipt_for_id

        app = Flask(__name__)
        app.config['TESTING'] = True

        with app.test_request_context('/process', method='POST', data='', content_type='application/json'):
            response = process_receipt_for_id()
            assert response.status_code == 400
            assert response.get_json() == {"error": [{"field": "unknown_field", "message": "field required"}]}