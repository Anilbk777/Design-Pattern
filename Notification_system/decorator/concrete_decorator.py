from interface.notification_decorator import NotificationDecorator
from datetime import datetime

class TimeStampDecorator(NotificationDecorator):
    def get_content(self, message: str):
        return f"{self._notification.get_content(message)} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"