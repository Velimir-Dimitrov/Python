year_tax = int(input())

shoes = year_tax - (year_tax * 0.4)
clothes = shoes - (shoes * 0.2)
ball = clothes / 4
accessories = ball / 5

total_cost = year_tax + shoes + clothes + ball + accessories
print(total_cost)
