import math
import logging


def calculate_description_points(receipt):
    """
    Award points for each item with a description length that is a multiple of 3.
    Points awarded are 20% of the item's price, rounded up to the nearest integer.
    
    Parameters:
    receipt (dict): A dictionary containing purchase details, including an "items" list.
                    Each item in the list should have "shortDescription" and "price" fields.
    
    Returns:
    int: Total points awarded based on the description length of each item.
    """
    points = 0
    for item in receipt.get("items", []):
        description = item.get("shortDescription", "").strip()
        
        # Validate and convert price
        try:
            price = float(item.get("price", "0"))
        except ValueError:
            price = 0  # Default to 0 if price is invalid

        # Check if description length is a multiple of 3
        if description and len(description) % 3 == 0:
            points += math.ceil(price * 0.2)
    
    return points
