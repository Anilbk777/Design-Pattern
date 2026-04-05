from abc import ABC, abstractmethod

class NotificationStrategy(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class EmailNotificationStrategy(NotificationStrategy):
    def send(self, message: str):
        print(f"[Email Notification]: {message}")

class SMSNotificationStrategy(NotificationStrategy):
    def send(self, message: str):
        print(f"[SMS Notification]: {message}")

class PushNotificationStrategy(NotificationStrategy):
    def send(self, message: str):
        print(f"[Push Notification]: {message}")
