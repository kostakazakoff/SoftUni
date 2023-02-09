class Helper:

    @staticmethod
    def validate_phone_number(phone: str, message):
        if not all((phone.startswith('0'), len(phone) == 10, phone.isdigit())):
            raise ValueError(message)

    @staticmethod
    def validate_name_not_empty_str(name: str, message):
        if not name:
            raise ValueError(message)

    @staticmethod
    def validate_price_more_than_0(price: float, message):
        if price <= 0:
            raise ValueError(message)

    @staticmethod
    def find_registered_client_by_phone_number(phone_number: str, clients_list: list):
        for client in clients_list:
            if client.phone_number == phone_number:
                return client

    @staticmethod
    def check_if_menu_is_ready(menu):
        if len(menu) < 5:
            raise Exception("The menu is not ready!")

    @staticmethod
    def find_meal_in_menu(meal_name, menu):
        for m in menu:
            if m.name == meal_name:
                return m
        raise Exception(f"{meal_name} is not on the menu!")

    @staticmethod
    def check_for_order(client):
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

    @staticmethod
    def reset_shopping(client):
        client.ordered_meals_quantities.clear()
        client.shopping_cart.clear()
        client.bill = 0

    @staticmethod
    def check_meal_quantity(meal, quantity):
        if meal.quantity < quantity:
            raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal.name}!")
