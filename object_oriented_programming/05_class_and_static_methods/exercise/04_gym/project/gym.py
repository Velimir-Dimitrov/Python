from typing import List
from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.get_obj(subscription_id, self.subscriptions)
        customer = self.get_obj(subscription.customer_id, self.customers)
        trainer = self.get_obj(subscription.trainer_id, self.trainers)
        plan = self.get_obj(subscription.trainer_id, self.plans)
        equipment = self.get_obj(plan.equipment_id, self.equipment)
        result = f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"
        return result

    @staticmethod
    def get_obj(some_id: int, some_objs: list):
        return next((obj for obj in some_objs if some_id == obj.id))

