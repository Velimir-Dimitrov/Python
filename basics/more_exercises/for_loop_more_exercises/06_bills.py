months = int(input())

electricity = 0
water = 0
internet = 0
other = 0

for _ in range(months):
    current_electricity = float(input())
    electricity += current_electricity
    water += 20
    internet += 15
    other += (current_electricity + 35) * 1.2

average = (electricity + water + internet + other) / months

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {average:.2f} lv")
