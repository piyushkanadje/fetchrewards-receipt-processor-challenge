def calculate_item_pair_points(receipt):
    """
    Award 5 points for every two items on the receipt.
    
    Parameters:
    receipt (dict): A dictionary containing purchase details, including an "items" list.
    
    Returns:
    int: Total points awarded based on pairs of items.
    """
    items = receipt.get("items", [])

    # Ensure items is a list
    if not isinstance(items, list):
        return 0
    
    # Calculate points for every pair of items
    return (len(items) // 2) * 5
