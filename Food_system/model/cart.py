from .restaurant import Restaurant
from .menu_item import MenuItem

from typing import Optional

class Cart:
    def __init__(self, restaurant:Optional[Restaurant] =None):
        self._restaurant = restaurant
        self._items:list[MenuItem] = []

    def add_item(self, item:MenuItem):
        if not self._restaurant:
            raise ValueError("Cart: Set a restaurant before adding items.")

        self._items.append(item)

    def get_total_cost(self):
        return sum(item.price for item in self._items)

    def is_empty(self):
        return self._restaurant is None or len(self._items) == 0

    def clear(self):
        self._items.clear()
        self._restaurant = None

    # Optional setters/getters
    def set_restaurant(self, restaurant: Restaurant):
        self._restaurant = restaurant

    def get_restaurant(self) -> Optional[Restaurant]:
        return self._restaurant

    def get_items(self) -> list[MenuItem]:
        return self._items.copy()
