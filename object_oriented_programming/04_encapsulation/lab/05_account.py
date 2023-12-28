from typing import Optional


class Account:
    def __init__(self, _id: int, balance: int, pin: int):
        self._id = _id
        self.balance = balance
        self.pin = pin

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, value):
        self.__pin = value

    def get_id(self, pin: int) -> Optional[str]:
        if pin == self.__pin:
            return self.__id
        return "Wrong pin"

    def change_pin(self, old_pin: int, new_pin: int) -> str:
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"


# Test code:
account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
