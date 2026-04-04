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
