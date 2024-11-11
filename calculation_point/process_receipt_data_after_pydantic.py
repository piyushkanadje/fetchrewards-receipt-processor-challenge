from datetime import date, time

def preprocess_receipt_data(receipt):
    # Convert purchaseDate to "YYYY-MM-DD" string format if it's a date object
    if isinstance(receipt.get("purchaseDate"), date):
        receipt["purchaseDate"] = receipt["purchaseDate"].isoformat()
    
    # Convert purchaseTime to "HH:MM" string format if it's a time object
    if isinstance(receipt.get("purchaseTime"), time):
        receipt["purchaseTime"] = receipt["purchaseTime"].strftime("%H:%M")
    
    return receipt