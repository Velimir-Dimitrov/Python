from project.animal import Animal


class Cheetah(Animal):
    def __init__(self, name, gender, age):
        Animal.__init__(self, name, gender, age, money_for_care=60)
