import math
from datetime import datetime
from calculation_point.purchase_time_points import calculate_time_points
from calculation_point.odd_day_points import calculate_day_points
from calculation_point.total_amount_points import calculate_total_points
from calculation_point.item_pair_points import calculate_item_pair_points
from calculation_point.description_points import calculate_description_points
from calculation_point.alphanumric_points import calculate_alphanumeric_points
from calculation_point.process_receipt_data_after_pydantic import preprocess_receipt_data

def calculate_total_receipt_points(receipt):
    """
    Aggregate points from all calculation functions for a given receipt.
    """
    
    # Preprocess date and time fields before calculations
    receipt = preprocess_receipt_data(receipt)
    
    calculators = [
        calculate_alphanumeric_points,
        calculate_day_points,
        calculate_time_points,
        calculate_total_points,
        calculate_item_pair_points,
        calculate_description_points
    ]
    
    # Calculate total points by applying each calculator function
    return sum(calculator(receipt) for calculator in calculators)