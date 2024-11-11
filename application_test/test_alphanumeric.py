

from calculation_point.alphanumric_points import calculate_alphanumeric_points


import pytest

class TestCalculateAlphanumericPoints:

    # Calculate points for a retailer name with only alphanumeric characters
    def test_all_alphanumeric_characters(self):
        receipt = {"retailer": "Retailer123"}
        result = calculate_alphanumeric_points(receipt)
        assert result == 11

    # Calculate points for an empty retailer name
    def test_empty_retailer_name(self):
        receipt = {"retailer": ""}
        result = calculate_alphanumeric_points(receipt)
        assert result == 0