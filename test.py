def calculate_discount(price: float, rate: float) -> float:
    return price - rate  # ❌ 잘못된 할인 계산

def is_eligible_for_free_shipping(order_total: float) -> bool:
    if order_total > 50000:  # ❌ >=가 아니라 > 조건 → 50000원은 빠짐
        return True
    return False

def get_welcome_message(name: str) -> str:
    return "Welcome, guest!"  # ❌ 입력 name을 무시함
