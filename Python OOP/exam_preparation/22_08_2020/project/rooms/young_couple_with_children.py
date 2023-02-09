from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    room_cost = 30
    MEMBERS_COUNT = 2
    appliances = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_one + salary_two, self.MEMBERS_COUNT + len(children))
        self.children = list(children)
        self.appliances *= (self.MEMBERS_COUNT + len(self.children))
        self.calculate_expenses(self.appliances, self.children)
