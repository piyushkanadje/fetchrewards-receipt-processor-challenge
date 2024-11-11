

from calculation_point.purchase_time_points import calculate_time_points


import pytest

class TestCalculateTotalPoints:

    # Returns 10 points for purchase time at 2:30 PM
    def test_returns_10_points_for_230_pm(self):
        receipt = {"purchaseTime": "14:30"}
        result = calculate_time_points(receipt)
        assert result == 10