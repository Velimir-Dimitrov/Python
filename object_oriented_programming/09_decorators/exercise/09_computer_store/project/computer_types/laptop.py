from project.computer_types.computer import Computer
from math import log2, ceil, floor


def is_power_of_two(n):
    return ceil(log2(n)) == floor(log2(n))


def logarithm_base(n):
    return int(log2(n))


class Laptop(Computer):
    processor_dict = {"AMD Ryzen 9 5950X": 900,
                      "Intel Core i9-11900H": 1050,
                      "Apple M1 Pro": 1200}
    MAX_RAM_SIZE = 64

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.processor_dict:
            raise ValueError(f"{processor} is not compatible with laptop"
                             f" {self.manufacturer} {self.model}!")
        if not is_power_of_two(ram) or ram > self.MAX_RAM_SIZE:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop"
                             f" {self.manufacturer} {self.model}!")
        self.processor = processor
        self.ram = ram
        processor_price = self.processor_dict[processor]
        ram_price = logarithm_base(ram) * 100
        self.price += processor_price + ram_price
        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."
