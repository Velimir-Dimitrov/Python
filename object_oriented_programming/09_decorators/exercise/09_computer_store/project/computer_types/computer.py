from abc import ABC, abstractmethod


class Computer(ABC):
    types = ["Laptop", "Desktop Computer"]

    def __init__(self, manufacturer: str, model: str, processor: str = None, ram: int = None, price: int = 0):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = processor
        self.ram = ram
        self.price = price

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.isspace() or len(value) == 0:
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.isspace() or len(value) == 0:
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @abstractmethod
    def configure_computer(self, processor:str, ram: int):
        pass

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"

