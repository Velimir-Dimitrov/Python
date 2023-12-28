from calculations import *

numbers_operating_string = input().split()
number_one, operator, number_two = numbers_operating_string
print(f"{mapper[operator](float(number_one), int(number_two)):.2f}")