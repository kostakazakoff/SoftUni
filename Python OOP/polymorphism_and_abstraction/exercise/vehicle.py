from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
    
    @abstractmethod
    def drive():
        pass

    @abstractmethod
    def refuel():
        pass


class Car(Vehicle):
    CONDITIONER_CONSUMPTION = 0.9

    def drive(self, distance):
        consumption = distance * (self.fuel_consumption + __class__.CONDITIONER_CONSUMPTION)
        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONDITIONER_CONSUMPTION = 1.6

    def drive(self, distance):
        consumption = distance * (self.fuel_consumption + __class__.CONDITIONER_CONSUMPTION)
        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95