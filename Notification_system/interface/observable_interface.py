from abc import ABC, abstractmethod

class ObservableInterface(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def unregister_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass
