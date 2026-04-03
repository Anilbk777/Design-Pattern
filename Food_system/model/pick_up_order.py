from .order import Order

class PickupOrder(Order):
    def __init__(self):
        super().__init__()
        self.restaurant_address: str = ""

    def get_type(self) -> str:
        return "Pickup"

    def set_restaurant_address(self, addr: str):
        self.restaurant_address = addr

    def get_restaurant_address(self) -> str:
        return self.restaurant_address
