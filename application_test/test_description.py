

from calculation_point.description_points import calculate_description_points


import pytest

class TestCalculateDescriptionPoints:

    # Calculates points correctly when all item descriptions have lengths that are multiples of 3
    def test_all_descriptions_multiple_of_three(self):
        receipt = {
            "items": [
                {"shortDescription": "abc", "price": "10"},
                {"shortDescription": "defghi", "price": "15"},
                {"shortDescription": "jklmno", "price": "20"}
            ]
        }
        assert calculate_description_points(receipt) == 9  # 2 + 3 + 4 = 9

    # Handles an empty receipt gracefully
    def test_empty_receipt(self):
        receipt = {"items": []}
        assert calculate_description_points(receipt) == 0