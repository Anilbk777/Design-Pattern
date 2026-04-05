from interface.notification_decorator import NotificationDecorator
from datetime import datetime

class TimeStampDecorator(NotificationDecorator):

    def __init__(self, notification: NotificationInterface):
        super().__init__(notification)

    def get_content(self, message: str):
        return f"[Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {self._notification.get_content(message)}"

class SignatureDecorator(NotificationDecorator):

    def __init__(self, notification: NotificationInterface):
        super().__init__(notification)

    def get_content(self, message: str):
        return f"{self._notification.get_content(message)} [Signature: Admin]"