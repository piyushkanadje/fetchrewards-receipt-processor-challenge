

from calculation_point.process_receipt_data_after_pydantic import preprocess_receipt_data


import pytest

class TestPreprocessReceiptData:

    # Converts date object to ISO format string
    def test_convert_date_to_iso_format(self):
        from datetime import date
        receipt = {"purchaseDate": date(2023, 10, 5)}
        result = preprocess_receipt_data(receipt)
        assert result["purchaseDate"] == "2023-10-05"

    # Handles receipt with missing "purchaseDate" key
    def test_missing_purchase_date_key(self):
        receipt = {"purchaseTime": "12:30"}
        result = preprocess_receipt_data(receipt)
        assert "purchaseDate" not in result