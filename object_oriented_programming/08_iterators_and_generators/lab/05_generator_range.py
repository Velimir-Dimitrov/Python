def genrange(start: int, end: int):
    while start <= end:
        temp = start
        start += 1
        yield temp


# Test code:
print(list(genrange(1, 10)))