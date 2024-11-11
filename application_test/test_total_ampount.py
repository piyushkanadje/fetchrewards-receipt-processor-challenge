

from calculation_point.total_amount_points import calculate_total_points


import pytest

class TestCalculateTotalPoints:

    # Calculate 50 points for round dollar totals
    def test_round_dollar_totals(self):
        receipt = {"total": "100.00"}
        assert calculate_total_points(receipt) == 50

    # Handle non-numeric total strings gracefully
    def test_non_numeric_total_string(self):
        receipt = {"total": "abc"}
        assert calculate_total_points(receipt) == 0