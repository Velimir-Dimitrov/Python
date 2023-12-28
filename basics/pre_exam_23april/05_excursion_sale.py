sea_excursions = int(input())
mountain_excursions = int(input())

sea_price = 680
mountain_price = 499
profit = 0

while sea_excursions > 0 or mountain_excursions > 0:
    command = input()

    if command == "Stop":
        break
    elif command == "sea":
        if sea_excursions == 0:
            continue
        else:
            sea_excursions -= 1
            profit += sea_price
    elif command == "mountain":
        if mountain_excursions == 0:
            continue
        else:
            mountain_excursions -= 1
            profit += mountain_price

if sea_excursions == 0 and mountain_excursions == 0:
    print("Good job! Everything is sold.")
print(f'Profit: {profit} leva.')