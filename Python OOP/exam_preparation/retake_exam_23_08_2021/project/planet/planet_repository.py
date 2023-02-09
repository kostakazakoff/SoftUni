from project.planet.planet import Planet


class PlanetRepository:
    def __init__(self):
        self.planets = []

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        if planet in self.planets:
            self.planets.remove(planet)

    def find_by_name(self, name: str):
        planet_found = [x for x in self.planets if x.name == name]
        if planet_found:
            return planet_found[0]
