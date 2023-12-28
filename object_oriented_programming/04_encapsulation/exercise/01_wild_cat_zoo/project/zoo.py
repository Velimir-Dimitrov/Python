from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list = []
        self.workers: list = []

    def add_animal(self, animal: Animal, price: int)-> str:
        if self.__animal_capacity > len(self.animals):
            if self.__budget - price >= 0:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str)-> str:
        for worker in self.workers:
            if worker_name == worker.name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salaries = sum([worker.salary for worker in self.workers])
        if self.__budget - total_salaries >= 0:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_animal_care = sum([animal.money_for_care for animal in self.animals])
        if self.__budget - total_animal_care >= 0:
            self.__budget -= total_animal_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        result = f"You have {len(self.animals)} animals"
        animals_categorised = {"Lion": [], "Tiger": [], "Cheetah": []}
        [animals_categorised[animal.__class__.__name__].append(animal) for animal in self.animals]
        for type_of_animal, animals in animals_categorised.items():
            result += f"\n----- {len(animals_categorised[type_of_animal])} {type_of_animal}s:"
            for current_animal in animals:
                result += '\n' + repr(current_animal)
        return result

    def workers_status(self) -> str:
        result = f"You have {len(self.workers)} workers"
        workers_categorised = {"Keeper": [], "Caretaker": [], "Vet": []}
        [workers_categorised[worker.__class__.__name__].append(worker) for worker in self.workers]
        for type_of_worker, workers in workers_categorised.items():
            result += f"\n----- {len(workers_categorised[type_of_worker])} {type_of_worker}s:"
            for current_worker in workers:
                result += "\n" + repr(current_worker)
        return result
