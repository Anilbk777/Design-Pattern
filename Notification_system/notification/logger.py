from interface.observer_interface import ObserverInterface
# from interface.observable_interface import ObservableInterface
from notification.notification_observable import NotificationObservable

class Logger(ObserverInterface):
    def __init__(self):
        self._message = None

    def update(self, notification: NotificationObservable):
        self._message = notification.get_notification()
        self.log()

    def log(self):
        print(f"[Logger] {self._message}")