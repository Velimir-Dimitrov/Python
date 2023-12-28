years = int(input())
washing_machine = float(input())
price_toy = int(input())

even_money = 0
brother_money = 0
odd_money = 0

for age in range(1, years + 1):
    if age % 2 != 0:
        odd_money += price_toy
    else:
        even_money += 10 * (age / 2)
        brother_money += 1

savings = odd_money + even_money - brother_money
diff = abs(washing_machine - savings)

if savings >= washing_machine:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
