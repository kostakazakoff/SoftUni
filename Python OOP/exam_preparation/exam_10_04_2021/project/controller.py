from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    VALID_AQUARIUM_TYPES = {"FreshwaterAquarium": FreshwaterAquarium, "SaltwaterAquarium": SaltwaterAquarium}
    VALID_DECORATION_TYPES = {"Ornament": Ornament, "Plant": Plant}
    VALID_FISH_TYPES = {"FreshwaterFish": FreshwaterFish, "SaltwaterFish": SaltwaterFish}
    VALID_FISH_AQUARIUM = {"FreshwaterFish": "FreshwaterAquarium", "SaltwaterFish": "SaltwaterAquarium"}

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.VALID_AQUARIUM_TYPES:
            return "Invalid aquarium type."
        self.aquariums.append(self.VALID_AQUARIUM_TYPES[aquarium_type](aquarium_name))
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.VALID_DECORATION_TYPES:
            return "Invalid decoration type."
        self.decorations_repository.add(self.VALID_DECORATION_TYPES[decoration_type]())
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if not decoration:
            return f"There isn't a decoration of type {decoration_type}."
        aquarium = next(filter(lambda x: x.name == aquarium_name, self.aquariums), None)
        if aquarium:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in self.VALID_FISH_TYPES:
            return f"There isn't a fish of type {fish_type}."
        aquarium = next(filter(lambda x: x.name == aquarium_name, self.aquariums))
        if not aquarium:
            return
        if self.VALID_FISH_AQUARIUM[fish_type] != aquarium.__class__.__name__:
            return "Water not suitable."
        aquarium.add_fish(self.VALID_FISH_TYPES[fish_type](fish_name, fish_species, price))

    def feed_fish(self, aquarium_name: str):
        aquarium = next(filter(lambda x: x.name == aquarium_name, self.aquariums))
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = next(filter(lambda x: x.name == aquarium_name, self.aquariums))
        decorations_value = sum(x.price for x in aquarium.decorations)
        fish_value = sum(x.price for x in aquarium.fish)
        aquarium_value = decorations_value + fish_value
        return f"The value of Aquarium {aquarium_name} is {aquarium_value}."

    def report(self):
        output = []
        for aquarium in self.aquariums:
            output.append(str(aquarium))
        return '\n'.join(output)
