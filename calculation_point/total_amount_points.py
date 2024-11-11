def calculate_total_points(receipt):
    """Award points based on total amount: 50 points for round dollar, 25 points for multiple of 0.25."""
    total_str = receipt.get("total", "0")
    try:
        total = float(total_str)
        points = 50 if total.is_integer() else 0
        points += 25 if total % 0.25 == 0 else 0
        return points
    except ValueError:
        return 0