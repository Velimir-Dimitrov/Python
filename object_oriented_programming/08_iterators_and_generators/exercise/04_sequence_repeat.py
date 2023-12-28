class sequence_repeat:
    def __init__(self, some_sequence: str, times_repeat: int):
        self.some_sequence = some_sequence
        self.times_repeat = times_repeat
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.times_repeat:
            raise StopIteration
        char = self.some_sequence[self.iterations % len(self.some_sequence)]
        self.iterations += 1
        return char


# Test codes:
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
