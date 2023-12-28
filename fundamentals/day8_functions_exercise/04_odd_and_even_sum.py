def odd_and_even_sum(num):
    str_num = str(num)
    even_sum = 0
    odd_sum = 0
    for index in range(len(str_num)):
        num_check = str_num[index]
        if int(num_check) % 2 == 0:
            even_sum += int(num_check)
        else:
            odd_sum += int(num_check)
    return odd_sum, even_sum


number = int(input())
sum_of_odd_digits, sum_of_even_digits = odd_and_even_sum(number)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")