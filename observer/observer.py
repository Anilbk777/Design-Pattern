from abc import ABC, abstractmethod

class FitnessDataObserver(ABC):

    @abstractmethod
    def update(self, subejct:"FitnessDataSubject"):
        pass

class FitnessDataSubject(ABC):

    @abstractmethod
    def register_observer(self, observer: FitnessDataObserver):
        pass

    @abstractmethod
    def remove_observer(self, observer: FitnessDataObserver):
        pass

    @abstractmethod
    def notify(self):
        pass

class FitnessData(FitnessDataSubject):
    def __init__(self):
        self.steps = 0
        self.active_minutes = 0
        self.calories = 0
        self.observers :list[FitnessDataObserver] = []

    def register_observer(self, observer:FitnessDataObserver):
        if not isinstance(observer, FitnessDataObserver):
            raise ValueError("Give observer is not an instance of FitnessDataObserver")
        
        self.observers.append(observer)
    