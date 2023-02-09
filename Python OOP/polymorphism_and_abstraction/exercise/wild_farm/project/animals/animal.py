from abc import ABC, abstractmethod
from food import Food


class Animal(ABC):
    def __init__(self, name: str, weight: float, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @abstractmethod
    def make_sound(self):
        pass

    @property
    @abstractmethod
    def weight_increase(self):
        pass

    @property
    @abstractmethod
    def eats(self) -> list:
        pass

    def feed(self, food: Food):
        if type(food) not in self.eats:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.food_eaten += food.quantity
        self.weight += food.quantity * self.weight_increase


class Bird(Animal, ABC):
    @abstractmethod
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    @abstractmethod
    def __init__(self, name: str, weight: float, living_region: float):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"