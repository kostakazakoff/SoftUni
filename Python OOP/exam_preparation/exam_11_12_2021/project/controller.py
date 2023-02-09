from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race
from project.helper import Helper


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        available_types = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}
        if model in [x.model for x in self.cars]:
            raise Exception(f"Car {model} is already created!")
        if car_type in available_types:
            car = available_types[car_type](model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        Helper.check_duplicated_driver(self.drivers, driver_name)
        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if race_name in [x.name for x in self.races]:
            raise Exception(f"Race {race_name} is already created!")
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = Helper.find_driver(self.drivers, driver_name)
        new_car = Helper.find_new_car(self.cars, car_type)
        new_car.is_taken = True
        new_model = new_car.model
        if driver.car:
            old_model = driver.car.model
            driver.car.is_taken = None
            driver.car = new_car
            return f"Driver {driver_name} changed his car from {old_model} to {new_model}."
        driver.car = new_car
        return f"Driver {driver_name} chose the car {new_model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = Helper.find_race(self.races, race_name)
        driver = Helper.find_driver(self.drivers, driver_name)
        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            raise Exception(f"Driver {driver_name} is already added in {race_name} race.")
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = Helper.find_race(self.races, race_name)
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        fastest_drivers = Helper.top_3(race)
        for driver in fastest_drivers:
            driver.number_of_wins += 1
        return '\n'.join([f"Driver {d.name} wins the {race_name} "
                          f"race with a speed of {d.car.speed_limit}."
                          for d in fastest_drivers])
