from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    POSITION_EARNINGS = {}
    race_expenses = 0

    @abstractmethod
    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        race_earnings = 0
        for sponsors in self.__class__.POSITION_EARNINGS.values():
            for position, earning in sponsors.items():
                if race_pos <= position:
                    race_earnings += earning
                    break
        race_revenue = race_earnings - self.__class__.race_expenses
        self.budget += race_revenue
        return f"The revenue after the race is {race_revenue}$. Current budget {self.budget}$"

