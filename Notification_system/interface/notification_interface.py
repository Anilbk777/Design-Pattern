from abc import ABC, abstractmethod

class NotificationInterface(ABC):
    @abstractmethod
    def get_content(self, message: str):
        pass
