from .menu_item import MenuItem

class Restaurant:
    RESTAURANT_ID = 0

    def __init__(self, name:str, address: str):
        self._name = name
        self._address = address
        self._menu: list[MenuItem] = []
        self.restaurant_id = Restaurant.RESTAURANT_ID + 1


    @property
    def name(self):
        return self._name
    
    def set_name(self, n:str):
        self._name = n

    @property
    def address(self):
        return self._address
    
    def set_address(self,addr:str):
        self._address =addr

    @property
    def menu(self):
        return self._menu.copy()
    
    def add_menu_item(self,menu_item:MenuItem):
        self._menu.append(menu_item)

    

