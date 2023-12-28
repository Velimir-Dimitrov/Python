from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    POSITION_EARNINGS = {"Oracle": {1: 1500000, 2: 800000}, "Honda": {8: 20000, 10: 10000}}
    race_expenses = 250000

    def __init__(self, budget: int):
        super().__init__(budget)
