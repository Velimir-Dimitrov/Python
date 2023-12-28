def smallest_num(num1, num2, num3):
    num_list = [num1, num2, num3]
    return min(num_list)


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
print(smallest_num(number_1, number_2, number_3))
