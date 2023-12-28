cost_of_vacation = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

profit = number_of_puzzles * 2.60 + number_of_dolls * 3 + number_of_bears * 4.10 + number_of_minions * 8.20 + number_of_trucks * 2
number_order = number_of_puzzles + number_of_dolls + number_of_bears + number_of_minions + number_of_trucks

if number_order >= 50:
    profit *= 0.75

profit *= 0.9
diff = abs(cost_of_vacation - profit)

if profit >= cost_of_vacation:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')

