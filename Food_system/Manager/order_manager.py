from model import Order
from .singleton import singleton

@singleton
class OrderManager:

    def __init__(self):
        self.orders:list[Order] = []

    def add_order(self, order: "Order"):
        self.orders.append(order)

    def list_orders(self):
        print("\n--- All Orders ---")
        for order in self.orders:
            print(
                f"{order.get_type()} order for {order.get_user().get_name()} | "
                f"Total: ₹{order.get_total()} | At: {order.get_scheduled()}"
            )
