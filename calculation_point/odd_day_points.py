def calculate_day_points(receipt):
    """
    Award 6 points if the purchase day is odd.
    
    Parameters:
    receipt (dict): A dictionary containing purchase details, including "purchaseDate" in "YYYY-MM-DD" format.
    
    Returns:
    int: 6 points if the purchase day is odd, 0 otherwise.
    """
    purchase_date = receipt.get("purchaseDate")
    if purchase_date:
        day = int(purchase_date.split("-")[-1])
        return 6 if day % 2 != 0 else 0
    return 0