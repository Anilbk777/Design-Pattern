from abc import ABC, abstractmethod
from interface.observable_interface import ObservableInterface

class ObserverInterface(ABC):
    @abstractmethod
    def update(self, notification: ObservableInterface):
        pass