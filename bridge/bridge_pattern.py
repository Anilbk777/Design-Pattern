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
        print(f"Driving the {self.name} car in the highway.")
