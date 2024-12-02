from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Model name cannot be empty.")      
        self.__model = value

    def __repr__(self) -> str:
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"

    @property
    @abstractmethod
    def processors(self):
        ...

    @property
    @abstractmethod
    def max_ram(self):
        ...

    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        ...

    @staticmethod
    def ram_is_valid(ram_size):
        return log2(ram_size) == int(log2(ram_size))
