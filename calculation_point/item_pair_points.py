
def calculate_item_pair_points(receipt):
    """Award 5 points for every two items on the receipt."""
    items = receipt.get("items", [])
    return (len(items) // 2) * 5