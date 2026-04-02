from abc import ABC, abstractmethod

class Pizza:

    def __init__(self, name:str):
        self.name = name
    
    def __repr__(self):
        return f"{self.name}"
    
class NYCheesePizza(Pizza):

    def __init__(self):
        super().__init__("NY style cheese pizza (thin crust)")

class NYPepperoniPizza(Pizza):

    def __init__(self):
        super().__init__("NY style pepperoni pizza ( thin crust)")

class ChicagoCheesePizza(Pizza):

    def __init__(self):
        super().__init__("Chicago style cheese pizza (deep dish)")

class ChicagoPepperoniPizza(Pizza):

    def __init__(self):
        super().__init__("Chicago style pepperoni pizza (deep dish)")


class PizzaStore(ABC):

    @abstractmethod
    def create_pizza(self, pizza_type:str) -> Pizza:
        pass

    def order_pizza(self, pizza_type:str) -> Pizza:
        pizza = self.create_pizza(pizza_type)
        print(f"[Preparing: {pizza}]")
        return f"ready :{pizza}"
    
class NYPizzaStore(PizzaStore):

    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return NYCheesePizza()

        elif pizza_type == "pepperoni":
            return NYPepperoniPizza()
        
        else:
            raise ValueError(f"Unknow NY pizza type: {pizza_type}")
        

class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):

        if pizza_type == "cheese":
            return ChicagoCheesePizza()

        elif pizza_type == "pepperoni":
            return ChicagoPepperoniPizza()
        
        else:
            raise ValueError(f"Unknow Chicago pizza type: {pizza_type}")
        

if __name__ == "__main__":
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()

    pizza1 = ny_store.order_pizza("cheese")
    print(pizza1)

    pizza2 = chicago_store.order_pizza("pepperoni")
    print(pizza2)

    




        