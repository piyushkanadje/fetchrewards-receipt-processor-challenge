from pydantic import BaseModel, Field, field_validator
from typing import List
from datetime import date, time

class Item(BaseModel):
    shortDescription: str = Field(
        ...,
        pattern=r"^[\w\s\-]+$",  # Updated from regex to pattern
        description="The Short Product Description for the item.",
        example="Mountain Dew 12PK"
    )
    price: str = Field(
        ...,
        pattern=r"^\d+\.\d{2}$",  # Updated from regex to pattern
        description="The total price paid for this item.",
        example="6.49"
    )

    @field_validator("shortDescription")
    def validate_short_description(cls, value):
        if len(value.strip()) == 0:
            raise ValueError("shortDescription cannot be empty or just whitespace.")
        return value

class Receipt(BaseModel):
    retailer: str = Field(
        ...,
        pattern=r"^[\w\s\-&]+$",  # Updated from regex to pattern
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
    items: List[Item] = Field(
        ...,
        min_items=1,
        description="A list of items purchased."
    )
    total: str = Field(
        ...,
        pattern=r"^\d+\.\d{2}$",  # Updated from regex to pattern
        description="The total amount paid on the receipt.",
        example="6.49"
    )

    @field_validator("retailer")
    def validate_retailer(cls, value):
        if len(value.strip()) == 0:
            raise ValueError("retailer cannot be empty or just whitespace.")
        return
