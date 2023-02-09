class Helper:

    @staticmethod
    def check_duplicated_driver(drivers: list, driver_name: str):
        if driver_name in [x.name for x in drivers]:
            raise Exception(f"Driver {driver_name} is already created!")

    @staticmethod
    def find_driver(drivers: list, driver_name: str):
        driver = [x for x in drivers if x.name == driver_name]
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        return driver[0]

    @staticmethod
    def find_race(races: list, race_name: str):
        race = [x for x in races if x.name == race_name]
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        return race[0]

    @staticmethod
    def find_new_car(cars: list, car_type: str):
        new_car = [x for x in cars if x.__class__.__name__ == car_type and not x.is_taken]
        if car_type not in ["MuscleCar", "SportsCar"] or not new_car:
            raise Exception(f"Car {car_type} could not be found!")
        return new_car[-1]

    @staticmethod
    def top_3(race):
        fastest = sorted([x for x in race.drivers], key=lambda x: -x.car.speed_limit)[:3]
        return fastest
