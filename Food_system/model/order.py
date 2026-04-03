from typing import List, Optional
from abc import ABC, abstractmethod

from .user import User
from .restaurant import Restaurant
from .menu_item import MenuItem
from ..strategies.payment_strategy import PaymentStrategy

class Order(ABC):
    next_order_id = 0  # class-level static variable

    def __init__(self):
        type(self).next_order_id += 1
        self.order_id: int = type(self).next_order_id
        self.user: Optional["User"] = None
        self.restaurant: Optional["Restaurant"] = None
        self.items: List["MenuItem"] = []
        self.payment_strategy: Optional["PaymentStrategy"] = None
        self.total: float = 0.0
        self.scheduled: str = ""

    # Payment handling
    def process_payment(self) -> bool:
        if self.payment_strategy:
            self.payment_strategy.pay(self.total)
            return True
        else:
            print("Please choose a payment mode first")
            return False

    # Abstract method for order type
    @abstractmethod
    def get_type(self) -> str:
        pass

    # Getters / Setters
    def set_user(self, user: "User"):
        self.user = user

    def get_user(self) -> Optional["User"]:
        return self.user

    def set_restaurant(self, restaurant: "Restaurant"):
        self.restaurant = restaurant

    def get_restaurant(self) -> Optional["Restaurant"]:
        return self.restaurant

    def set_items(self, items: List["MenuItem"]):
        self.items = items
        self.total = sum(item.get_price() for item in items)

    def get_items(self) -> List["MenuItem"]:
        return self.items

    def set_payment_strategy(self, strategy: "PaymentStrategy"):
        self.payment_strategy = strategy

    def set_scheduled(self, scheduled: str):
        self.scheduled = scheduled

    def get_scheduled(self) -> str:
        return self.scheduled

    def get_total(self) -> float:
        return self.total

    def set_total(self, total: float):
        self.total = total
