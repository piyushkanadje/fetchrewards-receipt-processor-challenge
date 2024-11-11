def calculate_day_points(receipt):
    """Award 6 points if the purchase day is odd."""
    purchase_date = receipt.get("purchaseDate")
    if purchase_date:
        day = int(purchase_date.split("-")[-1])
        return 6 if day % 2 != 0 else 0
    return 0