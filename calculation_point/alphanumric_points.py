def calculate_alphanumeric_points(receipt):
    """Calculate points for each alphanumeric character in the retailer's name."""
    retailer_name = receipt.get("retailer", "")
    return sum(1 for char in retailer_name if char.isalnum())