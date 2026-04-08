from abc import ABC, abstractmethod

class Engine(ABC):

    @abstractmethod
    def start():
        pass

class PetrolEngine(Engine):
    
    def start():
        print("Petrol Engine start.")

class DieselEngine(Engine):

    def start():
        print("Diesel Engine start.")

class ElectricEngine(Engine):
    def start():
        print("Electric Engine start.")