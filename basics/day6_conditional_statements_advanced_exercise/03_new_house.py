type_flower = input()
number_flowers = int(input())
budget = int(input())
flower_price = 0
cost = 0
order = 0

if type_flower == "Roses":
    order = number_flowers * 5
    if number_flowers > 80:
        cost = order - (order * 0.10)
    else:
        cost = order
elif type_flower == "Dahlias":
    order = number_flowers * 3.80
    if number_flowers > 90:
        cost = order - (order * 0.15)
    else:
        cost = order
elif type_flower == "Tulips":
    order = number_flowers * 2.80
    if number_flowers > 80:
        cost = order - (order * 0.15)
    else:
        cost = order
elif type_flower == "Narcissus":
    order = number_flowers * 3
    if number_flowers < 120:
        cost = order + (order * 0.15)
    else:
        cost = order
elif type_flower == "Gladiolus":
    order = number_flowers * 2.50
    if number_flowers < 80:
        cost = order + (order * 0.20)
    else:
        cost = order

diff = abs(budget - cost)

if budget < cost:
    print(f"Not enough money, you need {diff:.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {number_flowers} {type_flower} and {diff:.2f} leva left.")