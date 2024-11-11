from datetime import date, time

def preprocess_receipt_data(receipt):
    if isinstance(receipt.get("purchaseDate"), date):
        receipt["purchaseDate"] = receipt["purchaseDate"].isoformat()
    
    if isinstance(receipt.get("purchaseTime"), time):
        receipt["purchaseTime"] = receipt["purchaseTime"].strftime("%H:%M")
    
    return receipt