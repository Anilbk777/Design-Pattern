from .singleton import singleton
from ..model.restaurant import Restaurant

@singleton
class RestaurantManager:  

    def __init__(self):
        self._restaurants: list[Restaurant] = []

    def add_restaurant(self, resturant:Restaurant):
        self._restaurants.append(resturant)

    def search_by_address(self, addr:str):
        result = [resturant for resturant in self._restaurants if resturant.address.lower() == addr.lower()]
        return result
