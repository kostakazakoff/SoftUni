from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def duplicated_food_or_drink(self, order_type, name):
        if name in [x.name for x in self.food_menu] or name in [x.name for x in self.drinks_menu]:
            raise Exception(f"{order_type} {name} is already in the menu!")

    def duplicated_table(self, table_number):
        if table_number in [x.table_number for x in self.tables_repository]:
            raise Exception(f"Table {table_number} is already in the bakery!")

    def find_free_table(self, number_of_people):
        table = [x for x in self.tables_repository if x.capacity >= number_of_people]
        if table:
            return table[0]

    def get_all_from_menu(self):
        menu = {x.name: x for x in self.food_menu}
        menu.update({x.name: x for x in self.drinks_menu})
        return menu

    def order_from_menu(self, table, orders_names: list, order_type: str):
        menu = self.get_all_from_menu()
        in_menu, not_in_menu = [], []

        for item in orders_names:
            if item in menu and order_type == "Food":
                table.order_food(menu[item])
                in_menu.append(str(menu[item]))
            elif item in menu and order_type == "Drink":
                table.order_drink(menu[item])
                in_menu.append(str(menu[item]))
            else:
                not_in_menu.append(item)

        output = [f"Table {table.table_number} ordered:"]
        [output.append(x) for x in in_menu]
        output.append(f"{self.name} does not have in the menu:")
        [output.append(x) for x in not_in_menu]

        return '\n'.join(output)

    def find_table_by_number(self, number):
        table = [x for x in self.tables_repository if x.table_number == number]
        return table

    def add_food(self, food_type: str, name: str, price: float):
        available_food = {"Bread": Bread, "Cake": Cake}
        if food_type in available_food and not self.duplicated_food_or_drink(food_type, name):
            self.food_menu.append(available_food[food_type](name, price))
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        available_drinks = {"Tea": Tea, "Water": Water}
        if drink_type in available_drinks and not self.duplicated_food_or_drink(drink_type, name):
            self.drinks_menu.append(available_drinks[drink_type](name, portion, brand))
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        available_types = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}
        if table_type in available_types and not self.duplicated_table(table_number):
            self.tables_repository.append(available_types[table_type](table_number, capacity))
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = self.find_free_table(number_of_people)
        if not table:
            return f"No available table for {number_of_people} people"
        table.reserve(number_of_people)
        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = self.find_table_by_number(table_number)
        if not table:
            return f"Could not find table {table_number}"
        table = table[0]
        return self.order_from_menu(table, list(food_names), 'Food')

    def order_drink(self, table_number: int, *drinks_name):
        table = self.find_table_by_number(table_number)
        if not table:
            return f"Could not find table {table_number}"
        table = table[0]
        return self.order_from_menu(table, list(drinks_name), 'Drink')

    def leave_table(self, table_number: int):
        table = self.find_table_by_number(table_number)
        if not table:
            return f"Could not find table {table_number}"
        table = table[0]
        table_bill = table.get_bill()
        self.total_income += table_bill
        table.clear()
        return f"Table: {table_number}\nBill: {table_bill:.2f}"

    def get_free_tables_info(self):
        return '\n'.join([table.free_table_info() for table in self.tables_repository if not table.is_reserved])

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
