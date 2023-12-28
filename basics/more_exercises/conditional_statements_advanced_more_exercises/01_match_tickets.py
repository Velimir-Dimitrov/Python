budget = float(input())
category = input()
people = int(input())

price = 0

if category == "VIP":
    price = 499.99
elif category == "Normal":
    price = 249.99

total_cost = price * people


if people <= 4:
    budget *= 0.25
elif 5 <= people <= 9:
    budget *= 0.4
elif 10 <= people <= 24:
    budget *= 0.5
elif 25 <= people <= 49:
    budget *= 0.6
else:
    budget *= 0.75

diff = abs(total_cost - budget)


if budget > total_cost:
    print(f"Yes! You have {diff:.2f} leva left.")
elif budget < total_cost:
    print(f"Not enough money! You need {diff:.2f} leva.")