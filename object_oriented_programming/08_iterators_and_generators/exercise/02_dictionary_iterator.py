class dictionary_iter:
    def __init__(self, dict_obj: dict):
        self.dict_obj = dict_obj
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == len(self.dict_obj):
            raise StopIteration
        index = self.start
        self.start += 1
        return list(self.dict_obj.items())[index]


# Test codes:
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
