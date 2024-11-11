def calculate_time_points(receipt):
    """
    Award 10 points if the purchase time is between 2:01 PM and 3:59 PM.
    
    Parameters:
    receipt (dict): A dictionary containing purchase details, including "purchaseTime" in "HH:MM" format.
    
    Returns:
    int: 10 points if purchase time falls within the specified range, 0 otherwise.
    """
    purchase_time = receipt.get("purchaseTime", "")
    try:
        if purchase_time:
            hour, minute = map(int, purchase_time.split(":"))
            # Check if time is between 2:01 PM and 3:59 PM
            if (hour == 14 and minute >= 1) or (hour == 15 and minute < 60):
                return 10
    except (ValueError, TypeError):
        # Log an error if the time format is incorrect (optional)
        pass
    return 0
