from notification_service import NotificationService
from notification.notification_engine import NotificationEngine
from strategy.notification_strategy import EmailNotificationStrategy, SMSNotificationStrategy, PushNotificationStrategy
from notification.logger import Logger
from notification.simple_notification import SimpleNotification
from decorator.concrete_decorator import TimeStampDecorator, SignatureDecorator

def main():
    service = NotificationService.get_instance()
    observable = service.get_observable()

    logger = Logger()
    engine = NotificationEngine()

    email_strategy = EmailNotificationStrategy()
    sms_strategy = SMSNotificationStrategy()
    push_strategy = PushNotificationStrategy()

    engine.set_strategy(email_strategy)
    engine.set_strategy(sms_strategy)
    engine.set_strategy(push_strategy)

    observable.register_observer(logger)
    observable.register_observer(engine)

    # Create Notification
    notification = SimpleNotification("Hello World")
    notification = TimeStampDecorator(notification)
    notification = SignatureDecorator(notification)

    service.send_notification(notification)


if __name__ == "__main__":
    main()
