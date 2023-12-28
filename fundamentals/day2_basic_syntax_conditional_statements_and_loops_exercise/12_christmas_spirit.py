quantity = int(input())
days = int(input())
points = 0
cost = 0

for current_day in range(1, days + 1):
    if current_day % 11 == 0:
        quantity += 2
    if current_day % 2 == 0:
        cost += 2 * quantity
        points += 5
    if current_day % 3 == 0:
        cost += 8 * quantity
        points += 13
    if current_day % 5 == 0:
        cost += 15 * quantity
        points += 17
        if current_day % 3 == 0:
            points += 30
    if current_day % 10 == 0:
        points -= 20
        cost += 23
    if current_day == days and current_day % 10 == 0:
        points -= 30
print(f"Total cost: {cost}")
print(f"Total spirit: {points}")
