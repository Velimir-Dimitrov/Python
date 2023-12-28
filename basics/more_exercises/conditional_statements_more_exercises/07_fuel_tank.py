type = input()
current_litres = float(input())

if type == "Diesel" or type == "Gas" or type == "Gasoline":
    if current_litres >= 25:
        print(f'You have enough {type.lower()}.')
    elif current_litres < 25:
        print(f'Fill your tank with {type.lower()}!')
else:
    print("Invalid fuel!")