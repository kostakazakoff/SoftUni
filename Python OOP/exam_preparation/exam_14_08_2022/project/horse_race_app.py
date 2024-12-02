from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    HORSE_TYPES_REF = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def find_jockey(self, j_name):
        result = [j for j in self.jockeys if j.name == j_name]
        if not result:
            raise Exception(f"Jockey {j_name} could not be found!")
        return result[0]

    def find_race(self, r_type):
        result = [r for r in self.horse_races if r.race_type == r_type]
        if not result:
            raise Exception(f"Race {r_type} could not be found!")
        return result[0]

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_name in [h.name for h in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.HORSE_TYPES_REF:
            self.horses.append(self.HORSE_TYPES_REF[horse_type](horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if jockey_name in [j.name for j in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in [r.race_type for r in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")

        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.find_jockey(jockey_name)

        horse_exist = [h for h in self.horses if h.__class__.__name__ == horse_type and not h.is_taken]
        if not horse_exist:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        horse = horse_exist[-1]

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.find_race(race_type)
        jockey = self.find_jockey(jockey_name)

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.find_race(race_type)

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        fastest = sorted(race.jockeys, key=lambda j: -j.horse.speed)[0]
        return f"The winner of the {race_type} race, with a speed of {fastest.horse.speed}km/h "\
               f"is {fastest.name}! Winner's horse: {fastest.horse.name}."
