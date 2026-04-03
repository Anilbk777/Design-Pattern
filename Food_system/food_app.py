from model import *
from strategies.payment_strategy import PaymentStrategy

from services.notification_services import NotificationService

from factory.now_order_factory import NowOrderFactory
from factory.schedule_order_factory import ScheduledOrderFactory

from Manager.order_manager import OrderManager
from Manager.restaurant_manager import RestaurantManager
from datetime import datetime
from typing import List, Optional


class FoodApp:
    def __init__(self):
        self.initialize_restaurants()

    def initialize_restaurants(self):
        restaurant1 = Restaurant("Mahalaxmi Dhaba", "Kathmandu")
        restaurant1.add_menu_item(MenuItem("P1", "Dal Bhat", 120))
        restaurant1.add_menu_item(MenuItem("P2", "Momo", 150))
        restaurant1.add_menu_item(MenuItem("P3", "Sel Roti", 50))

        restaurant2 = Restaurant("Annapurna Cafe", "Pokhara")
        restaurant2.add_menu_item(MenuItem("P1", "Thukpa", 90))
        restaurant2.add_menu_item(MenuItem("P2", "Sukuti", 80))
        restaurant2.add_menu_item(MenuItem("P3", "Chatamari", 70))

        restaurant3 = Restaurant("Gurung Dhaba", "Chitwan")
        restaurant3.add_menu_item(MenuItem("P1", "Dhindo", 100))
        restaurant3.add_menu_item(MenuItem("P2", "Kwati", 110))
        restaurant3.add_menu_item(MenuItem("P3", "Gundruk Soup", 60))


        restaurant_manager = RestaurantManager()
        restaurant_manager.add_restaurant(restaurant1)
        restaurant_manager.add_restaurant(restaurant2)
        restaurant_manager.add_restaurant(restaurant3)

    def search_restaurants(self, location: str) -> List[Restaurant]:
        return RestaurantManager().search_by_location(location)

    def select_restaurant(self, user: User, restaurant: Restaurant):
        if user.get_cart() is None:
            user.create_cart(restaurant)   # create + assign
        else:
            user.get_cart().set_restaurant(restaurant)

    def add_to_cart(self, user: User, item_code: str):
        restaurant = user.get_cart().get_restaurant()
        if not restaurant:
            print("Please select a restaurant first.")
            return

        for item in restaurant.get_menu():
            if item.get_code() == item_code:
                user.get_cart().add_item(item)
                break

    def checkout_now(
        self, user: User, order_type: str, payment_strategy: Optional[PaymentStrategy]
    ) -> Optional[Order]:
        return self.checkout(user, order_type, payment_strategy, NowOrderFactory())

    def checkout_scheduled(
        self,
        user: User,
        order_type: str,
        payment_strategy: Optional[PaymentStrategy],
        schedule_time: str,
    ) -> Optional[Order]:
        return self.checkout(
            user, order_type, payment_strategy, ScheduledOrderFactory(schedule_time)
        )

    def checkout(
        self,
        user: User,
        order_type: str,
        payment_strategy: Optional[PaymentStrategy],
        order_factory,
    ) -> Optional[Order]:
        if user.get_cart().is_empty():
            return None

        user_cart = user.get_cart()
        ordered_restaurant = user_cart.get_restaurant()
        items_ordered = user_cart.get_items()
        total_cost = user_cart.get_total_cost()

        order = order_factory.create_order(
            user,
            user_cart,
            ordered_restaurant,
            items_ordered,
            payment_strategy,
            total_cost,
            order_type,
        )
        OrderManager().add_order(order)
        return order

    def pay_for_order(self, user: User, order: Order):
        is_payment_success = order.process_payment()
        if is_payment_success:
            NotificationService.notify(order)
            user.get_cart().clear()

    def print_user_cart(self, user: User):
        print("Items in cart:")
        print("------------------------------------")
        for item in user.get_cart().get_items():
            print(f"{item.get_code()} : {item.get_name()} : ₹{item.get_price()}")
        print("------------------------------------")
        print(f"Grand total : ₹{user.get_cart().get_total_cost()}")
