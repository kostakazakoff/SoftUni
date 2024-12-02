from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @property
    @abstractmethod
    def sponsors(self):
        pass

    @property
    @abstractmethod
    def race_expenses(self):
        pass

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        for positions in self.sponsors.values():
            for must_position in positions:
                if race_pos <= must_position:
                    revenue += positions[must_position]
                    break
        revenue -= self.race_expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
