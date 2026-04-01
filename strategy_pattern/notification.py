from abc import ABC, abstractmethod

class NotificationStrategy(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class EmailNotification(NotificationStrategy):
    def send(self, message:str):
        print(f"Sending email: {message}")

class SMSNotification(NotificationStrategy):
    def send(self, message:str):
        print(f"Sending SMS: {message}")

class PushNotification(NotificationStrategy):
    def send(self, message:str):
        print(f"Sending Push Notification: {message}")

class NotificationContext:
    def __init__(self, strategy:NotificationStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy:NotificationStrategy):
        self._strategy = strategy

    def notify(self, message:str):
        self._strategy.send(message)

if __name__ == "__main__":
    email_notification = EmailNotification()
    sms_notification = SMSNotification()
    push_notification = PushNotification()

    context = NotificationContext(email_notification)
    context.notify("This is an email notification")

    context.set_strategy(sms_notification)
    context.notify("This is an SMS notification")

    context.set_strategy(push_notification)
    context.notify("This is a push notification")