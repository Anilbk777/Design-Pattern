from abc import ABC, abstractmethod
from interface.notification_interface import NotificationInterface

class NotificationDecorator(NotificationInterface):
    def __init__(self, notification: NotificationInterface):
        self._notification = notification

    @abstractmethod
    def get_content(self, message: str):
        pass