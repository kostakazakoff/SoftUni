from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    POSSIBLE_FISH_TYPES = ["FreshwaterFish", "SaltwaterFish"]

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(x.comfort for x in self.decorations)

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."

        if fish.__class__.__name__ in self.POSSIBLE_FISH_TYPES:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        [fish.eat() for fish in self.fish]

    def __str__(self):
        fish = ' '.join([f.name for f in self.fish]) if self.fish else 'none'
        return f"{self.name}:\nFish: {fish}\nDecorations: {len(self.decorations)}\n" \
               f"Comfort: {self.calculate_comfort()}"
