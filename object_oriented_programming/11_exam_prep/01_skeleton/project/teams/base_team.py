from abc import ABC, abstractmethod


class BaseTeam(ABC):

    def __init__(self, name: str, country:str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins: int = 0
        self.equipment: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        avr_protection_sum = int(sum(equipment.protection for equipment in self.equipment) / len(self.equipment)
                                 ) if self.equipment else 0

        result = (f"Name: {self.name}\n"
                  f"Country: {self.country}\n"
                  f"Advantage: {self.advantage} points\n"
                  f"Budget: {self.budget:.2f}EUR\n"
                  f"Wins: {self.wins}\n"
                  f"Total Equipment Price: {sum(equipment.price for equipment in self.equipment):.2f}\n"
                  f"Average Protection: {avr_protection_sum}")
        return result


