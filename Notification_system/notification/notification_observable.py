from interface.observable_interface import ObservableInterface
from interface.observer_interface import ObserverInterface
from interface.notification_interface import NotificationInterface

class NotificationObservable(ObservableInterface):
    def __init__(self):
        self._notification: NotificationInterface = None
        self._observers: list[ObserverInterface] = []

    def register_observer(self, observer: ObserverInterface):
        if not isinstance(observer, ObserverInterface):
            raise TypeError("Observer must be an instance of ObserverInterface")
        self._observers.append(observer)

    def unregister_observer(self, observer: ObserverInterface):
        if not isinstance(observer, ObserverInterface):
            raise TypeError("Observer must be an instance of ObserverInterface")
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

    def set_notification(self, notification: NotificationInterface):
        if not isinstance(notification, NotificationInterface):
            raise TypeError("Notification must be an instance of NotificationInterface")
        self._notification = notification
        self.notify_observers()

    def get_notification(self):
        return self._notification
