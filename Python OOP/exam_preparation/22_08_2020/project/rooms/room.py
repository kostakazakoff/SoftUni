class Room:
    room_cost = 0

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        for sublist in args:
            self.expenses += sum(x.get_monthly_expense() for x in sublist)

    @property
    def monthly_total_consumption(self):
        return self.expenses + self.room_cost

    def __repr__(self) -> str:
        output = [f'{self.family_name} with {self.members_count} members. '\
                f'Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$']

        total_room_children_expenses = 0
        for i, child in enumerate(self.children, 1):
            monthly_child_expenses = child.get_monthly_expense()
            total_room_children_expenses += monthly_child_expenses
            output.append(f'--- Child {i} monthly cost: {monthly_child_expenses:.2f}$')

        output.append(f'--- Appliances monthly cost: {(self.expenses - total_room_children_expenses):.2f}$')

        return '\n'.join(output)
