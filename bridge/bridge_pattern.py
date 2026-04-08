from abc import ABC, abstractmethod

class Engine(ABC):

    @abstractmethod
    def start():
        pass

class PetrolEngine(Engine):
    
    def start():
        print("Petrol Engine start.")

        