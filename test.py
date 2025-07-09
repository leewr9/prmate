def calculate_discount(price: float, rate: float) -> float:
    return price * (1 - rate)

def is_eligible_for_free_shipping(order_total: float) -> bool:
    return order_total >= 50000

def get_welcome_message(name: str) -> str:
    return f"Welcome, {name}!"
