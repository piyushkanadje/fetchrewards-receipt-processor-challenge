
from receipt_processor.data_validation import Item
from receipt_processor.data_validation import Receipt
from datetime import date
from datetime import time
import pytest

class TestItem:

    # Validate shortDescription with valid alphanumeric characters
    def test_valid_short_description(self):
        item = Item(shortDescription="Mountain Dew 12PK", price="6.49")
        assert item.shortDescription == "Mountain Dew 12PK"

    # shortDescription is an empty string
    def test_empty_short_description(self):
        with pytest.raises(ValueError, match="shortDescription cannot be empty or just whitespace."):
            Item(shortDescription="", price="6.49")







class TestReceipt:

    # Valid retailer name with alphanumeric characters and special symbols
    def test_valid_retailer_name_with_special_symbols(self):
        from receipt_processor.data_validation import Item
        from datetime import date, time
        receipt = Receipt(
            retailer="M&M Corner Market",
            purchaseDate=date(2022, 1, 1),
            purchaseTime=time(13, 1),
            items=[Item(shortDescription="Mountain Dew 12PK", price="6.49")],
            total="6.49"
        )
        assert receipt.retailer == "M&M Corner Market"

    # Retailer name is empty or just whitespace
    def test_empty_retailer_name(self):
        from receipt_processor.data_validation import Item
        from datetime import date, time
        import pytest
        with pytest.raises(ValueError, match="Retailer field cannot be empty. Please provide the retailer name."):
            Receipt(
                retailer="   ",
                purchaseDate=date(2022, 1, 1),
                purchaseTime=time(13, 1),
                items=[Item(shortDescription="Mountain Dew 12PK", price="6.49")],
                total="6.49"
            )

    # Correctly formatted purchase date and time
    def test_purchase_date_and_time_format(self):
        from datetime import date, time
        from receipt_processor.data_validation import Receipt, Item

        items = [Item(shortDescription="Mountain Dew 12PK", price="6.49")]
        receipt = Receipt(
            retailer="M&M Corner Market",
            purchaseDate=date(2022, 1, 1),
            purchaseTime=time(13, 1),
            items=items,
            total="6.49"
        )

        assert receipt.purchaseDate == date(2022, 1, 1)
        assert receipt.purchaseTime == time(13, 1)

    # Total amount matches the sum of item prices
    def test_total_amount_matches_sum_of_items(self):
        from receipt_processor.data_validation import Receipt, Item

        items = [
            Item(shortDescription="Mountain Dew 12PK", price="6.49"),
            Item(shortDescription="Coca Cola 6PK", price="4.99")
        ]
        receipt = Receipt(
            retailer="M&M Corner Market",
            purchaseDate=date(2022, 1, 1),
            purchaseTime=time(13, 1),
            items=items,
            total="11.48"
        )

        assert receipt.total == "11.48"