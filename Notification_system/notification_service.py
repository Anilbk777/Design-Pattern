from notification.notification_observable import NotificationObservable
from interface.notification_interface import NotificationInterface

class NotificationService:
    _instance = None

    def __init__(self):
        self._observable = NotificationObservable()
        self._history:list[NotificationInterface] = []

    def get_instance(cls):
        if cls._instance is None:
            cls._instance = NotificationService()
        return cls._instance

    def send_notification(self, notification: NotificationInterface):
        try:
            if not isinstance(notification, NotificationInterface):
                raise TypeError("Notification must be an instance of NotificationInterface")
            self._history.append(notification)
            self._observable.set_notification(notification)
        except Exception as e:
            print(f"Error: {e}")

    def get_observable(self) -> NotificationObservable:
        return self._observable

    def get_history(self) -> list[str]:
        return [notification.get_content() for notification in self._history]

  