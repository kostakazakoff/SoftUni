from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    MEMBERS_COUNT = 2
    room_cost = 15
    appliances = [TV(), Fridge(), Stove()] * MEMBERS_COUNT

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one + pension_two, self.MEMBERS_COUNT)
        self.calculate_expenses(self.appliances)
