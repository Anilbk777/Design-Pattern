from abc import ABC, abstractmethod

class Engine(ABC):

    @abstractmethod
    def start(self):
        pass


class PetrolEngine(Engine):

    def start(self):
        print("Petrol Engine start.")


class DieselEngine(Engine):

    def start(self):
        print("Diesel Engine start.")


class ElectricEngine(Engine):

    def start(self):
        print("Electric Engine start.")


class Car(ABC):

    def __init__(self, name:str, engine:Engine):
        self.name = name
        self.engine = engine

    @abstractmethod
    def drive(self):
        pass


class Sedan(Car):

    def __init__(self, name:str, engine:Engine):
        super().__init__(name, engine)

    def drive(self):
        self.engine.start()
        print(f"Driving the {self.name} car in the highway.")

class SUV(Car):

    def __init__(self, name:str, engine:Engine):
        super().__init__(name, engine)

    def drive(self):
        self.engine.start()
        print(f"Driving the {self.name} car in the highway.")

class BYD(Car):
    def __init__(self, name:str, engine:Engine):
        super().__init__(name, engine)

    def drive(self):
        self.engine.start()
        print(f"Driving the {self.name} car in the highway.")


if __name__ == "__main__":
    petrol_engine = PetrolEngine()
    diesel_engine = DieselEngine()
    eletric_engine = ElectricEngine()

    sedan_car = Sedan("SEDAN",petrol_engine)
    sedan_car.drive()

    suv_car1 = SUV("SUV",petrol_engine)
    suv_car1.drive()
    suv_car2 = SUV("SUV", diesel_engine)
    suv_car2.drive()

    byd_car = BYD("BYD-2026", eletric_engine)
    byd_car.drive()