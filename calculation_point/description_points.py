import math
def calculate_description_points(receipt):
    """
    Award points for each item with description length multiple of 3.
    Points are 20% of the price, rounded up.
    """
    points = 0
    for item in receipt.get("items", []):
        description = item.get("shortDescription", "").strip()
        price = float(item.get("price", "0"))
        if len(description) % 3 == 0:
            points += math.ceil(price * 0.2)
    return points