
# Generated by Qodo Gen
from calculation_point.odd_day_points import calculate_day_points


import pytest

class TestCalculateDayPoints:

    # Returns 6 points for odd purchase days
    def test_odd_purchase_day_points(self):
        receipt = {"purchaseDate": "2023-10-05"}
        assert calculate_day_points(receipt) == 6

    # Handles missing "purchaseDate" key gracefully
    def test_missing_purchase_date_key(self):
        receipt = {}
        assert calculate_day_points(receipt) == 0