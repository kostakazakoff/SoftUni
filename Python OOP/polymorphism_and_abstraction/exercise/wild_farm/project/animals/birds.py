from animals.animal import Bird
from food import Vegetable, Fruit, Meat, Seed


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    @property
    def weight_increase(self):
        return 0.25

    @property
    def eats(self):
        return [Meat]


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    @property
    def weight_increase(self):
        return 0.35

    @property
    def eats(self) -> list:
        return [Vegetable, Fruit, Meat, Seed]