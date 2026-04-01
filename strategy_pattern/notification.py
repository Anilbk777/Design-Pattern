from abc import ABC, abstractmethod

class NotificationStrategy(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class EmailNotification(NotificationStrategy):
    def send(self, message:str):
        print(f"Sending email: {message}")

class SMSNotification(NotificationStrategy):
    def senf(self, message:str):
        print(f"Sending SMS: {message}")

