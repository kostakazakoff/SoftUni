from abc import ABC, abstractmethod
from project.helper import Helper


class Meal(ABC):
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Helper.validate_name_not_empty_str(value, "Name cannot be an empty string!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Helper.validate_price_more_than_0(value, "Invalid price!")
        self.__price = value

    @abstractmethod
    def details(self):
        ...
