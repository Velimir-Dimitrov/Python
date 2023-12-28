class vowels:
    def __init__(self, received_string):
        self.received_string = received_string
        self.vowels = "aeiouy"
        self.received_vowels = [char for char in self.received_string if char.lower() in self.vowels]
        self.index = -1
        self.end_index = len(self.received_vowels) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.end_index:
            raise StopIteration
        self.index += 1
        return self.received_vowels[self.index]


# Test code:
my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
