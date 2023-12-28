from typing import List
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.clients.adult import Adult


class BankApp:
    VALID_TYPES_OF_LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_TYPES_OF_CLIENTS = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_TYPES_OF_LOANS:
            raise Exception("Invalid loan type!")
        loan = self.VALID_TYPES_OF_LOANS[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_TYPES_OF_CLIENTS:
            raise Exception("Invalid client type!")
        elif self.capacity == len(self.clients):
            return "Not enough bank capacity."
        client = self.VALID_TYPES_OF_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan = next(l for l in self.loans if l.__class__.__name__ == loan_type)
        client = next(c for c in self.clients if client_id == c.client_id)
        if loan_type not in client.VALID_LOAN:
            raise Exception("Inappropriate loan type!")
        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = next((c for c in self.clients if client_id == c.client_id), None)

        if client is None:
            raise Exception("No such client!")
        elif client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = 0
        for l in self.loans:
            if l.__class__.__name__ == loan_type:
                l.increase_interest_rate()
                number_of_changed_loans += 1
        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = 0
        for c in self.clients:
            if min_rate > c.interest:
                c.increase_clients_interest()
                changed_client_rates_number += 1
        return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self):
        total_rates = [client.interest for client in self.clients]
        avg_client_interest_rate = sum(total_rates) / len(total_rates) if total_rates else 0
        result = (f"Active Clients: {len(self.clients)}",
                  f"Total Income: {sum(client.income for client in self.clients):.2f}",
                  f"Granted Loans: {sum(len(client.loans) for client in self.clients)}, "
                  f"Total Sum: {sum(sum(loan.amount for loan in client.loans) for client in self.clients):.2f}",
                  f"Available Loans: {len(self.loans)}, Total Sum: {sum(loan.amount for loan in self.loans):.2f}",
                  f"Average Client Interest Rate: {avg_client_interest_rate:.2f}")
        return "\n".join(result)
