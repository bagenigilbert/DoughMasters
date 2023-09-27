def validate_name(name):
    """Validate the name of a restaurant.

    Args:
        name (str): The name of the restaurant.

    Returns:
        bool: True if the name is valid, False otherwise.
        str: Error message if the name is not valid.
    """
    if len(name) > 50:
        return False, "Name must be less than 50 characters."
    return True, ""

def validate_price(price):
    """Validate the price of a restaurant pizza.

    Args:
        price (float): The price of the pizza.

    Returns:
        bool: True if the price is valid, False otherwise.
        str: Error message if the price is not valid.
    """
    if not 1 <= price <= 30:
        return False, "Price must be between 1 and 30."
    return True, ""
