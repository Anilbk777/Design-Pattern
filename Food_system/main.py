from food_app import FoodApp
from model.user import User
from strategies.esewa_payment_strategy import EsewaPaymentStrategy


def main():
    food = FoodApp()

    user = User(101, "Ram", "Pokhara")
    print(f"User: {user.get_name()} is active.")

    # User searches for restaurants by location
    restaurant_list = food.search_restaurants("Pokhara")

    if not restaurant_list:
        print("No restaurants found!")
        return

    print("Found Restaurants:")
    for restaurant in restaurant_list:
        print(f" - {restaurant.get_name()}")

    food.select_restaurant(user, restaurant_list[0])
    print(f"Selected restaurant: {restaurant_list[0].get_name()}")

    food.add_to_cart(user, "P1")
    food.add_to_cart(user, "P2")

    food.print_user_cart(user)

    payment_strategy = EsewaPaymentStrategy("1234567890")
    order = food.checkout_now(user, "Delivery", payment_strategy)

    if order:
        food.pay_for_order(user, order)


if __name__ == "__main__":
    main()
