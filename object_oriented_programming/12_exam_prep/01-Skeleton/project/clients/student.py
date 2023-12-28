from project.clients.base_client import BaseClient
from project.loans.student_loan import StudentLoan


class Student(BaseClient):
    VALID_LOAN = {"StudentLoan": StudentLoan}

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, 2.0)

    def increase_clients_interest(self):
        self.interest += 1
