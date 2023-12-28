from typing import List
from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.predatory_fish import PredatoryFish
from project.fish.deep_sea_fish import DeepSeaFish


class NauticalCatchChallengeApp:
    VALID_TYPES_DIVERS = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_TYPES_FISH = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_TYPES_DIVERS:
            return f"{diver_type} is not allowed in our competition."
        elif diver_name in [diver.name for diver in self.divers]:
            return f"{diver_name} is already a participant."
        diver = self.VALID_TYPES_DIVERS[diver_type](diver_name)
        self.divers.append(diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_TYPES_FISH:
            return f"{fish_type} is forbidden for chasing in our competition."
        elif fish_name in [fish.name for fish in self.fish_list]:
            return f"{fish_name} is already permitted."
        fish = self.VALID_TYPES_FISH[fish_type](fish_name, points)
        self.fish_list.append(fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = next((diver for diver in self.divers if diver_name == diver.name), None)
        fish = next((fish for fish in self.fish_list if fish_name == fish.name), None)
        if diver is None:
            return f"{diver_name} is not registered for the competition."
        elif fish is None:
            return f"The {fish_name} is not allowed to be caught in this competition."
        elif diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch or (diver.oxygen_level == fish.time_to_catch and not is_lucky):
            diver.miss(fish.time_to_catch)
            diver.has_health_issue = True
            return f"{diver_name} missed a good {fish_name}."
        diver.hit(fish)
        diver.has_health_issue = True if diver.oxygen_level == 0 else False
        return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        count = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.has_health_issue = False
                diver.oxygen_level = diver.__class__.OXYGEN_LEVEL
                count += 1
        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        diver = next(diver for diver in self.divers if diver_name == diver.name)
        result = [f"**{diver_name} Catch Report**"]
        for fish in diver.catch:
            result.append(fish.fish_details())
        return "\n".join(result)

    def competition_statistics(self):
        result = ["**Nautical Catch Challenge Statistics**"]
        divers = sorted(self.divers, key=lambda d: (-d.competition_points, (-len(d.catch), d.name)))
        for diver in divers:
            if not diver.has_health_issue:
                result.append(diver.__str__())
        return "\n".join(result)



