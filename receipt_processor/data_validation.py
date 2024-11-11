from pydantic import BaseModel, Field, field_validator, conlist,model_validator,root_validator
from typing import List
from datetime import date, time
import re
class Item(BaseModel):
    """
    Represents an item in the receipt data.

    Attributes:
        shortDescription (str): The Short Product Description for the item.
        price (str): The total price paid for this item.

    Validation Rules:
        shortDescription: Must not be empty or contain invalid characters.
            Valid characters: alphanumeric, spaces, hyphens, ampersands.
        price: Must be a positive decimal with two decimal places (e.g., '1.25').
    
    """


    shortDescription: str = Field(
        ...,
   
        description="The Short Product Description for the item.",
        example="Mountain Dew 12PK"
    )
    price: str = Field(
        ...,

        description="The total price paid for this item.",
        example="6.49"
    )

    @field_validator("shortDescription")
    def validate_short_description(cls, value):
        """
        Validate the shortDescription field.

        Args:
            cls (Item): The Item instance being validated.
            value (str): The value of the shortDescription field.

        Raises:
            ValueError: If the shortDescription is empty or contains invalid characters.

        Returns:
            str: The validated shortDescription value.
        """

        if len(value.strip()) == 0:
            raise ValueError("shortDescription cannot be empty or just whitespace.")
        if not re.match(r"^[\w\s\-&]+$", value):
            raise ValueError("Retailer name contains invalid characters.")
        return value

    @field_validator("price")
    def validate_price(cls, value):
        """
        Validate the price field.

        Args:
            cls (Item): The Item instance being validated.
            value (str): The value of the price field.

        Raises:
            ValueError: If the price is not a positive decimal with two decimal places.

        Returns:
            str: The validated price value.
        """
        if not re.match(r"^\d+\.\d{2}$", value):
            raise ValueError("Price must be a positive decimal with two decimal places (e.g., '1.25').")
        return value

class Receipt(BaseModel):
    """
    Represents a receipt with details about the purchase, items purchased, and total amount paid.

    Attributes:
        retailer (str): The name of the retailer or store the receipt is from.
        purchaseDate (date): The date of the purchase printed on the receipt.
        purchaseTime (time): The time of the purchase printed on the receipt. 24-hour time expected.
        items (conlist(Item, min_length=1)): A list of items purchased.
        total (str): The total amount paid on the receipt.

    Methods:
        validate_retailer: Validates the retailer field to ensure it's non-empty and contains only valid characters.
        validate_total: Validates the total amount paid on the receipt to ensure it matches the sum of item prices.
    """
    retailer: str = Field(
        ...,

        description="The name of the retailer or store the receipt is from.",
        example="M&M Corner Market"
    )
    purchaseDate: date = Field(
        ...,
        description="The date of the purchase printed on the receipt.",
        example="2022-01-01"
    )
    purchaseTime: time = Field(
        ...,
        description="The time of the purchase printed on the receipt. 24-hour time expected.",
        example="13:01"
    )
    items: conlist(Item, min_length=1) = Field(
        ...,
        min_items=1,
        description="A list of items purchased."
    )
    total: str = Field(
        ...,
  
        description="The total amount paid on the receipt.",
        example="6.49"
    )

    @field_validator("retailer")
    def validate_retailer(cls, value):
        """
        Validates the retailer field to ensure it's non-empty and contains only valid characters.

        :param cls: The class instance (not used in this method)
        :param value: The retailer name to be validated
        :raises ValueError: If the retailer field is empty or contains invalid characters
        :returns: The validated retailer name
        """
        if len(value.strip()) == 0:
            raise ValueError("Retailer field cannot be empty. Please provide the retailer name.")
        if not re.match(r"^[\w\s\-&]+$", value):
            raise ValueError("Retailer name contains invalid characters.")
        return value
    
    @model_validator(mode="after")
    def validate_total(cls, self):
        """
        Validates the total amount paid on the receipt to ensure it matches the sum of item prices.

        :param cls: The class instance (not used in this method)
        :param self: The Receipt model instance being validated
        :raises ValueError: If the total amount is invalid or doesn't match the sum of item prices
        :returns: The validated Receipt model instance
        """

        total = self.total
        items = self.items

        if total and not re.match(r"^\d+\.\d{2}$", total):
            raise ValueError("Total must be a positive decimal with two decimal places (e.g., '1.25').")

        if items and total:
            calculated_total = sum(float(item.price) for item in items)
            if abs(calculated_total - float(total)) > 0.01: 
                raise ValueError("Total does not match the sum of item prices.")
        
        return self
    

        
