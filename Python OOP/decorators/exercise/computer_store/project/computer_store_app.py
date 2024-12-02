from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profits = 0

    @property
    def available_types(self):
        return {"Desktop Computer": DesktopComputer, "Laptop": Laptop}

    def _find_computer(self, wanted_processor, wanted_ram, cl_budget):

        compatible_computer = []
        for computer in self.warehouse:
            valid_price = computer.price <= cl_budget
            valid_processor = wanted_processor == computer.processor
            valid_ram = computer.ram >= wanted_ram
            if all ([valid_price, valid_processor, valid_ram]):
                compatible_computer.append(computer)

        if not compatible_computer:
            raise Exception("Sorry, we don't have a computer for you.")

        # if there is more than one computer with compatible parameters, choosing the cheaper one:
        chosen_comp = sorted(compatible_computer, key=lambda x: x.price)[0]
        return chosen_comp

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.available_types:
            raise ValueError(f"{type_computer} is not a valid type computer!")
            
        new_computer = self.available_types[type_computer](manufacturer, model)
        configuration = new_computer.configure_computer(processor, ram)
        self.warehouse.append(new_computer)
        return configuration

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        computer = self._find_computer(wanted_processor, wanted_ram, client_budget)
        self.profits += client_budget - computer.price
        self.warehouse.remove(computer)
        return f"{computer} sold for {client_budget}$."
