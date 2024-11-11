def calculate_alphanumeric_points(receipt):
    """
    Calculate points for each alphanumeric character in the retailer's name.

    Args:
        receipt (dict): A dictionary containing the retailer's information, including their name.

    Returns:
        int: The total number of alphanumeric characters in the retailer's name.
    """

    retailer_name = receipt.get("retailer", "")
    return sum(1 for char in retailer_name if char.isalnum())