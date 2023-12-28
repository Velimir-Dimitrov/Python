days = int(input())
hours = int(input())

total = 0

for day in range(1, days + 1):
    cost_for_day = 0
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            cost = 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            cost = 1.25
        else:
            cost = 1
        cost_for_day += cost
        total += cost
    print(f"Day: {day} - {cost_for_day:.2f} leva")
print(f"Total: {total:.2f} leva")