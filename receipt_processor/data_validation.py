from pydantic import BaseModel, Field, field_validator, conlist,model_validator,root_validator
from typing import List
from datetime import date, time
import re
class Item(BaseModel):
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
        if len(value.strip()) == 0:
            raise ValueError("shortDescription cannot be empty or just whitespace.")
        if not re.match(r"^[\w\s\-&]+$", value):
            raise ValueError("Retailer name contains invalid characters.")
        return value

    @field_validator("price")
    def validate_price(cls, value):
        if not re.match(r"^\d+\.\d{2}$", value):
            raise ValueError("Price must be a positive decimal with two decimal places (e.g., '1.25').")
        return value

class Receipt(BaseModel):
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
        if len(value.strip()) == 0:
            raise ValueError("Retailer field cannot be empty. Please provide the retailer name.")
        if not re.match(r"^[\w\s\-&]+$", value):
            raise ValueError("Retailer name contains invalid characters.")
        return value
    
    @model_validator(mode="after")
    def validate_total(cls, self):
        total = self.total
        items = self.items

        # Check that total is provided and formatted correctly
        if total and not re.match(r"^\d+\.\d{2}$", total):
            raise ValueError("Total must be a positive decimal with two decimal places (e.g., '1.25').")

        # Calculate sum of item prices and compare with total if items are provided
        if items and total:
            calculated_total = sum(float(item.price) for item in items)
            if abs(calculated_total - float(total)) > 0.01:  # allow small rounding differences
                raise ValueError("Total does not match the sum of item prices.")
        
        return self

        
