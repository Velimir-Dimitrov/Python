string_of_nums = input().split()
abs_nums = [abs(float(el)) for el in string_of_nums]
print(abs_nums)