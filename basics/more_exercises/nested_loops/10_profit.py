number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
sum_money = int(input())

for x in range(0, number_1 + 1):
    for y in range(0, number_2 +1):
        for c in range(0, number_3 + 1):
            if x * 1 + y * 2 + c * 5 == sum_money:
                print(f"{x} * 1 lv. + {y} * 2 lv. + {c} * 5 lv. = {sum_money} lv.")