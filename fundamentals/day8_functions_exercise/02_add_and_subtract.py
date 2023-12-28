def sum_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(sum, num3):
    return sum - num3


def add_and_subtract(num1, num2, num3):
    sum_of_first_and_second_numbers = sum_numbers(number_1, number_2)
    sub_of_sum_and_third_num = subtract_numbers(sum_of_first_and_second_numbers, number_3)
    return sub_of_sum_and_third_num


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
print(add_and_subtract(number_1, number_2, number_3))