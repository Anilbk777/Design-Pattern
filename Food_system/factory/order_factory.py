from abc import ABC, abstractmethod
from typing import List, Optional
from model import User, Cart, Restaurant,MenuItem, Order
from  strategies.payment_strategy import PaymentStrategy

class OrderFactory(ABC):
    @abstractmethod
    def create_order(
        self,
        user: User,
        cart: "Cart",
        restaurant: "Restaurant",
        menu_items: List["MenuItem"],
        payment_strategy: Optional["PaymentStrategy"],
        total_cost: float,
        order_type: str,
    ) -> "Order":
        """
        Factory method to create an Order object.
        Must be implemented by subclasses.
        """
        pass
