from abc import ABC, abstractmethod
from interface.observer_interface import ObserverInterface

class ObservableInterface(ABC):
    @abstractmethod
    def register_observer(self, observer: ObserverInterface):
        pass

    @abstractmethod
    def unregister_observer(self, observer: ObserverInterface):
        pass

    @abstractmethod
    def notify_observers(self):
        pass
