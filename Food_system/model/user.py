from .cart import Cart
from typing import Optional
from .restaurant import Restaurant

class User:

    def __init__(self, id:int, name:str, address:str):
        self.id = id
        self._name = name
        self._address = address
        self._cart: Optional[Cart] = None

    def create_cart(self, restaurant: Restaurant) -> Cart:
        if self._cart is not None:
            raise Exception("User already has a cart.")
        self._cart = Cart(restaurant)
        return self._cart

    def clear_cart(self):
        if self._cart:
            self._cart.clear()
            self._cart = None

    # Getters / Setters
    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str):
        self._name = name

    def get_address(self) -> str:
        return self._address

    def set_address(self, address: str):
        self._address = address

 
    def get_cart(self) -> Optional[Cart]:
        return self._cart
