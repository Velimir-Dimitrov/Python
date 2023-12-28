def squares(num: int):
    current_num = 0
    end_num = num
    while current_num < end_num:
        current_num += 1
        yield current_num ** 2

# Test code:
print(list(squares(5)))