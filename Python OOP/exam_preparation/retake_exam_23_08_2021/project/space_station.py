from project.astronaut.astronaut_repository import AstronautRepository
from project.planet.planet_repository import PlanetRepository
from project.planet.planet import Planet
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist


class SpaceStation:
    
    __successful_missions = 0
    __uncompleted_missions = 0
    ASTRONAUT_TYPES = {"Biologist": Biologist, "Geodesist": Geodesist, "Meteorologist": Meteorologist}

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut:
            return f"{name} is already added."

        if astronaut_type not in self.ASTRONAUT_TYPES:
            raise Exception("Astronaut type is not valid!")
        
        astronaut = self.ASTRONAUT_TYPES[astronaut_type](name)
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        planet = self.planet_repository.find_by_name(name)
        if planet:
            return f"{name} is already added."
        planet = Planet(name)
        planet.items.extend(items.split(', '))
        self.planet_repository.planets.append(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)

        if not planet:
            raise Exception("Invalid planet name!")

        astronauts = sorted([x for x in self.astronaut_repository.astronauts \
                      if x.oxygen > 30], key=lambda a: a.oxygen)

        if not astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        astronauts = astronauts[-5:]
        astronauts_participated_count = 0

        while astronauts and planet.items:
            astronaut_out = astronauts.pop()
            astronauts_participated_count += 1
            while planet.items:
                if astronaut_out.oxygen <= 0:
                    break
                astronaut_out.backpack.append(planet.items.pop())
                astronaut_out.breathe()

        if planet.items:
            self.__uncompleted_missions += 1
            return "Mission is not completed."

        self.__successful_missions += 1
        return f"Planet: {planet_name} was explored. " \
               f"{astronauts_participated_count} astronauts participated in collecting items."

    def report(self):
        astronauts_info = '\n'.join([str(a) for a in self.astronaut_repository.astronauts])
        return f"{self.__successful_missions} successful missions!\n"\
                f"{self.__uncompleted_missions} missions were not completed!\n"\
                f"Astronauts' info:\n{astronauts_info}"
