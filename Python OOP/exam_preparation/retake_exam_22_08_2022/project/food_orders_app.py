from project.client import Client
from project.meals.meal import Meal
from project.helper import Helper


class FoodOrdersApp:
    AVAILABLE_MEALS = ['Starter', 'MainDish', 'Dessert']
    receipt_id = 1

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        if Helper.find_registered_client_by_phone_number(client_phone_number, self.clients_list):
            raise Exception("The client has already been registered!")
        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in self.AVAILABLE_MEALS:
                self.menu.append(meal)

    def show_menu(self):
        Helper.check_if_menu_is_ready(self.menu)
        return '\n'.join(meal.details() for meal in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        Helper.check_if_menu_is_ready(self.menu)
        client = Helper.find_registered_client_by_phone_number(client_phone_number, self.clients_list)
        if not client:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        prepared_order = {}
        prepared_order_bill = 0
        for meal_name, quantity in meal_names_and_quantities.items():
            meal = Helper.find_meal_in_menu(meal_name, self.menu)
            Helper.check_meal_quantity(meal, quantity)
            if meal not in prepared_order:
                prepared_order[meal] = 0
            prepared_order[meal] += quantity
            prepared_order_bill += quantity * meal.price

        for meal, quantity in prepared_order.items():
            if meal not in client.ordered_meals_quantities:
                client.ordered_meals_quantities[meal] = 0
            client.ordered_meals_quantities[meal] += quantity
            client.shopping_cart.append(meal)
            meal.quantity -= quantity

        client.bill += prepared_order_bill
        meal_names = ', '.join(m.name for m in client.shopping_cart)

        return f"Client {client_phone_number} successfully ordered {meal_names} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = Helper.find_registered_client_by_phone_number(client_phone_number, self.clients_list)
        Helper.check_for_order(client)
        
        for meal, meal_quantity in client.ordered_meals_quantities.items():
            meal.quantity += meal_quantity

        Helper.reset_shopping(client)
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = Helper.find_registered_client_by_phone_number(client_phone_number, self.clients_list)
        Helper.check_for_order(client)

        output = f"Receipt #{FoodOrdersApp.receipt_id} with total amount of {client.bill:.2f} "\
                 f"was successfully paid for {client_phone_number}."
        
        Helper.reset_shopping(client)
        self.receipt_id += 1
        return output

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} "\
               f"meals on the menu and {len(self.clients_list)} clients."
