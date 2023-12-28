from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    consumption_increase = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        real_consumption = self.consumption_increase + self.fuel_consumption
        current_fuel_used = real_consumption * distance
        if self.fuel_quantity >= current_fuel_used:
            self.fuel_quantity -= current_fuel_used

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    consumption_increase = 1.6
    tank_issue = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        real_consumption = self.consumption_increase + self.fuel_consumption
        current_fuel_used = real_consumption * distance
        if self.fuel_quantity >= current_fuel_used:
            self.fuel_quantity -= current_fuel_used

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.tank_issue


# Test code:
car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
