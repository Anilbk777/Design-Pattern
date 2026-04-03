from .order import Order

class DeliveryOrder(Order):
    def __init__(self):
        super().__init__()
        self.user_address: str = ""

    def get_type(self) -> str:
        return "Delivery"

    def set_user_address(self, addr: str):
        self.user_address = addr

    def get_user_address(self) -> str:
        return self.user_address
