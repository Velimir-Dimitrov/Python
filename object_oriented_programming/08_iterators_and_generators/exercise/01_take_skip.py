class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.iterations:
            raise StopIteration
        current_num = self.iterations * self.step
        self.iterations += 1
        return current_num


# Test codes:
numbers = take_skip(2, 6)
for number in numbers:
    print(number)


numbers = take_skip(10, 5)
for number in numbers:
    print(number)

