from interface.notification_decorator import NotificationDecorator
from datetime import datetime

class TimeStampDecorator(NotificationDecorator):

    def __init__(self, notification: NotificationInterface):
        super().__init__(notification)

    def get_content(self):
        return f"[Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {self._notification.get_content()}"

class SignatureDecorator(NotificationDecorator):

    def __init__(self, notification: NotificationInterface):
        super().__init__(notification)

    def get_content(self):
        return f"{self._notification.get_content()} [Signature: Admin]"