class reverse_iter:
    def __init__(self, some_iterable):
        self.some_iterable = some_iterable
        self.start_index = len(some_iterable) - 1
        self.end_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.end_index > self.start_index:
            raise StopIteration
        index = self.start_index
        self.start_index -= 1
        return self.some_iterable[index]


# Test code:
reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
