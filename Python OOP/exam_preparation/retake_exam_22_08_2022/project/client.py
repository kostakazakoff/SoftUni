from project.helper import Helper


class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0
        self.ordered_meals_quantities = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        Helper.validate_phone_number(value, "Invalid phone number!")
        self.__phone_number = value
