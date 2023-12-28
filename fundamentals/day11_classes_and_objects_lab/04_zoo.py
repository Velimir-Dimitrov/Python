class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
current_zoo = Zoo(zoo_name)
number = int(input())
for line in range(number):
    animal_info = input().split(" ")
    animal_species = animal_info[0]
    animal_name = animal_info[1]

    current_zoo.add_animal(animal_species, animal_name)
species_check = input()
print(current_zoo.get_info(species_check))
