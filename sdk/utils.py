def validate_pet_data(pet):
    """Validates the data for a new pet."""
    required_fields = ['id', 'name', 'category', 'status']
    for field in required_fields:
        if field not in pet:
            return False, f"Missing required field: {field}"
    return True, "Pet data is valid."

def validate_order_data(order):
    """Validates the data for a new order."""
    required_fields = ['id', 'petId', 'quantity', 'shipDate', 'status']
    for field in required_fields:
        if field not in order:
            return False, f"Missing required field: {field}"
    return True, "Order data is valid."
