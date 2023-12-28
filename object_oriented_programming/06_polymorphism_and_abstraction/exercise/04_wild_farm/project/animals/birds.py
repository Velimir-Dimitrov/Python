from project.animals.animal import Bird
from project.food import Food


class Owl(Bird):
    WEIGHT_INCREASE_FROM_FOOD = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food: Food):
        if food.__class__.__name__ != "Meat":
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * self.WEIGHT_INCREASE_FROM_FOOD
        self.food_eaten += food.quantity


class Hen(Bird):
    WEIGHT_INCREASE_FROM_FOOD = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        self.weight += food.quantity * self.WEIGHT_INCREASE_FROM_FOOD
        self.food_eaten += food.quantity
