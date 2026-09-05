def calculate_total(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity cannot be negative")

    return price * quantity


def calculate_discount(price, discount_percent):
    if price < 0 or discount_percent < 0:
        raise ValueError("Price and discount cannot be negative")

    discount = price * discount_percent / 100
    return price - discount