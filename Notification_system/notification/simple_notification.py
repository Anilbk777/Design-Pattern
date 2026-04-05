from interface.notification_interface import NotificationInterface

class SimpleNotification(NotificationInterface):

    def __init__(self, text:str):
        self._text = text 

    def get_content(self):
        return f"Simple Notification: {self._text}"