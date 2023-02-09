from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.helper import Helper


class ChristmasPastryShopApp:
    VALID_DELICACY_TYPES = {'Gingerbread': Gingerbread, 'Stolen': Stolen}
    VALID_BOOTH_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: list = []
        self.delicacies: list = []
        self.income: float = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        Helper.check_for_duplicated_delicacy(name, self.delicacies)
        Helper.check_valid_type_of_delicacy(type_delicacy, self.VALID_DELICACY_TYPES)
        delicacy = self.VALID_DELICACY_TYPES[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        Helper.check_for_duplicated_booth_number(booth_number, self.booths)
        Helper.check_valid_booth_type(type_booth, self.VALID_BOOTH_TYPES)
        booth = self.VALID_BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        booth = Helper.find_free_booth(number_of_people, self.booths)
        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = Helper.find_booth_by_number(booth_number, self.booths)
        delicacy = Helper.find_delicacy_by_name(delicacy_name, self.delicacies)
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = Helper.find_booth_by_number(booth_number, self.booths)
        orders_price = [x.price for x in booth.delicacy_orders]
        bill = booth.price_for_reservation + sum(orders_price)
        self.income += bill
        booth.reset_booth()
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
