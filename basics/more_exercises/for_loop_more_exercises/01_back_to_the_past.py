heritage_money = float(input())
end_year = int(input())

current_years = 18
start_year = 1800
spending_money = 0

for year in range(start_year, end_year + 1):
    if year % 2 == 0:
        spending_money += 12000
    else:
        spending_money += 12000 + current_years * 50
    current_years += 1
diff = abs(heritage_money - spending_money)
if spending_money <= heritage_money:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f'He will need {diff:.2f} dollars to survive.')