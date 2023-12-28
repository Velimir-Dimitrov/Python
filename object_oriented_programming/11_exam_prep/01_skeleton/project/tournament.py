from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT = {"ElbowPad": ElbowPad, "KneePad": KneePad}
    VALID_TEAMS = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: list = []
        self.teams: list = []

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT.keys():
            raise Exception("Invalid equipment type!")
        created_equipment = self.VALID_EQUIPMENT[equipment_type]()
        self.equipment.append(created_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAMS.keys():
            raise Exception("Invalid team type!")
        elif len(self.teams) == self.capacity:
            return "Not enough tournament capacity."
        created_team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(created_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        current_equipment = next(equipment_obj for equipment_obj in reversed(self.equipment) if equipment_type == equipment_obj.__class__.__name__)
        for team in self.teams:
            if team.name == team_name:
                if team.budget >= current_equipment.price:
                    self.equipment.remove(current_equipment)
                    team.equipment.append(current_equipment)
                    team.budget -= current_equipment.price
                    return f"Successfully sold {equipment_type} to {team_name}."
                else:
                    raise Exception("Budget is not enough!")

    def remove_team(self, team_name: str):
        current_team = next((team for team in self.teams if team.name == team_name), None)
        if current_team is None:
            raise Exception("No such team!")
        elif current_team.wins > 0:
            raise Exception(f"The team has {current_team.wins} wins! Removal is impossible!")
        self.teams.remove(current_team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        changed_prices = 0
        for equipment in self.equipment:
            if equipment_type == equipment.__class__.__name__:
                equipment.increase_price()
                changed_prices += 1
        return f"Successfully changed {changed_prices}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = next(team for team in self.teams if team.name == team_name1)
        team2 = next(team for team in self.teams if team.name == team_name2)
        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")
        team1_points = team1.advantage + sum(equipment.protection for equipment in team1.equipment)
        team2_points = team2.advantage + sum(equipment.protection for equipment in team2.equipment)
        if team1_points == team2_points:
            return "No winner in this game."
        winner_team = team1 if team1_points > team2_points else team2
        winner_team.win()
        return f"The winner is {winner_team.name}."

    def get_statistics(self):
        teams = sorted(self.teams, key=lambda t: -t.wins)
        result = [f"Tournament: {self.name}",
                  f"Number of Teams: {len(self.teams)}",
                  f"Teams:"]
        [result.append(team.get_statistics()) for team in teams]
        return "\n".join(result)



