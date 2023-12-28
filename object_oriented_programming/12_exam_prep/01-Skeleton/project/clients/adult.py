from project.clients.base_client import BaseClient
from project.loans.mortgage_loan import MortgageLoan


class Adult (BaseClient):
    VALID_LOAN = {"MortgageLoan": MortgageLoan}

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, 4.0)

    def increase_clients_interest(self):
        self.interest += 2
