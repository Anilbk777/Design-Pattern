from typing import List, Optional
from order_factory import OrderFactory
from model import User, Cart, Restaurant, MenuItem, Order
from ..strategies.payment_strategy import PaymentStrategy


class ScheduledOrderFactory(OrderFactory):
    def __init__(self, schedule_time: str):
        self.schedule_time = schedule_time

    def create_order(
        self,
        user: "User",
        cart: Cart,
        restaurant: "Restaurant",
        menu_items: List["MenuItem"],
        payment_strategy: Optional["PaymentStrategy"],
        total_cost: float,
        order_type: str,
    ) -> "Order":

        if order_type == "Delivery":
            order = DeliveryOrder()
            order.set_user_address(user.get_address())
        else:  # Pickup
            order = PickupOrder()
            order.set_restaurant_address(restaurant.get_location())

        order.set_user(user)
        order.set_restaurant(restaurant)
        order.set_items(menu_items)
        order.set_payment_strategy(payment_strategy)
        order.set_scheduled(self.schedule_time)
        order.set_total(total_cost)

        return order
