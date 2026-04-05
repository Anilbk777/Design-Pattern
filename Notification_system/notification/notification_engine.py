from strategy.notification_strategy import NotificationStrategy
from interface.observer_interface import ObserverInterface
from notification.notification_observable import NotificationObservable

class NotificationEngine(ObserverInterface):
    def __init__(self):
        self._strategys :list[NotificationStrategy] = []

    def update(self, notification: NotificationObservable):
        for strategy in self._strategys:
            strategy.send(notification.get_notification())

    def set_strategy(self, strategy: NotificationStrategy):
        if not isinstance(strategy, NotificationStrategy):
            raise TypeError("Strategy must be an instance of NotificationStrategy")
        self._strategys.append(strategy)

