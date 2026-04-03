from .user import User

class Order:
    def __init__(self, user:User):
        if user.cart is None or user.cart.is_empty():
            raise ValueError("User has no items in cart to create an order.")
