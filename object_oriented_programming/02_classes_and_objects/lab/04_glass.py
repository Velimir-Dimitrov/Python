class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, amount: int):
        if self.content + amount <= Glass.capacity:
            self.content += amount
            return f"Glass filled with {self.content} ml"
        return f"Cannot add {amount} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        return f"{Glass.capacity - self.content} ml left"


# Test code:
glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
