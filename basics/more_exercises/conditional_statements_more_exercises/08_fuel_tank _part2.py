type_of_fuel = input()
litres_fuel = float(input())
club_card = input()

cost = 0

if type_of_fuel == "Gasoline":
    cost = 2.22
    if club_card == "Yes":
        cost -= 0.18

if type_of_fuel == "Diesel":
    cost = 2.33
    if club_card == "Yes":
        cost -= 0.18

if type_of_fuel == "Gas":
    cost = 0.93
    if club_card == "Yes":
        cost -= 0.08

total_cost = litres_fuel * cost

if 20 <= litres_fuel <= 25:
    total_cost *= 0.92
elif litres_fuel > 25:
    total_cost *= 0.9

print(f'{total_cost:.2f} lv.')
