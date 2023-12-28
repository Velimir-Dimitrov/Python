from project.animals.animal import Mammal
from project.food import Food


class Mouse(Mammal):
    WEIGHT_INCREASE_FROM_FOOD = 0.10

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        if food.__class__.__name__ == "Meat" or food.__class__.__name__ == "Seed":
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * self.WEIGHT_INCREASE_FROM_FOOD
        self.food_eaten += food.quantity


class Dog(Mammal):
    WEIGHT_INCREASE_FROM_FOOD = 0.40

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if food.__class__.__name__ != "Meat":
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * self.WEIGHT_INCREASE_FROM_FOOD
        self.food_eaten += food.quantity


class Cat(Mammal):
    WEIGHT_INCREASE_FROM_FOOD = 0.30

    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        if food.__class__.__name__ == "Seed" or food.__class__.__name__ == "Fruit":
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * self.WEIGHT_INCREASE_FROM_FOOD
        self.food_eaten += food.quantity


class Tiger(Mammal):
    WEIGHT_INCREASE_FROM_FOOD = 1

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        if food.__class__.__name__ != "Meat":
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * self.WEIGHT_INCREASE_FROM_FOOD
        self.food_eaten += food.quantity
