

from calculation_point.item_pair_points import calculate_item_pair_points


import pytest

class TestCalculateItemPairPoints:

    # Calculate points for an even number of items
    def test_even_number_of_items(self):
        receipt = {"items": ["apple", "banana", "orange", "grape"]}
        result = calculate_item_pair_points(receipt)
        assert result == 10

    # Handle non-list items value gracefully
    def test_non_list_items_value(self):
        receipt = {"items": "not_a_list"}
        result = calculate_item_pair_points(receipt)
        assert result == 0