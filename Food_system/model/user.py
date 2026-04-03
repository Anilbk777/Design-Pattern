from .cart import Cart
class User:

    def __init__(self, id:int, name:str, address:str):
        self.id = id
        self._name = name
        self._address = address
        self._cart: Cart = None

    