from abc import ABC, abstractmethod

class Burger(ABC):
    @abstractmethod
    def prepare(self):
        pass

class VeggieBurger(Burger):
    def prepare(self):
        print("Preparing veggie burger")

class ChickenBurger(Burger):
    def prepare(self):
        print("Preparing chicken burger")

class MixedBurger(Burger):
    def prepare(self):
        print("Preparing mixed burger")

class BurgerFactory:
    def create_burger(self, type:str) -> Burger:
        match type:
            case "veggie":
                return VeggieBurger()
            case "chicken":
                return ChickenBurger()
            case "mixed":
                return MixedBurger()
            case _:
                raise ValueError("Invalid burger type")

if __name__ == "__main__":
    factory = BurgerFactory()
    burger = factory.create_burger("veggie")
    burger.prepare()

    burger = factory.create_burger("chicken")
    burger.prepare()

    burger = factory.create_burger("mixed")
    burger.prepare()

    burger = factory.create_burger("beef")
    burger.prepare()