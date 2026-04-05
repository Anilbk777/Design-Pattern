from interface.notification_interface import NotificationInterface

class SimpleNotification(NotificationInterface):
    def get_content(self, message: str):
        return f"Simple Notification: {message}"