from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    POSITION_EARNINGS = {"Petronas": {1: 1000000, 3: 500000}, "TeamViewer": {5: 100000, 7: 50000}}
    race_expenses = 200000

    def __init__(self, budget: int):
        super().__init__(budget)



