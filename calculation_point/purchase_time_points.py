
def calculate_time_points(receipt):
    """Award 10 points if the purchase time is between 2:01pm and 3:59pm."""
    purchase_time = receipt.get("purchaseTime", "")
    if purchase_time:
        hour, minute = map(int, purchase_time.split(":"))
        if hour == 14 or (hour == 15 and minute == 0):
            return 10
    return 0