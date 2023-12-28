budget = float(input())
season = input()

type_car = ""
car_class = ""
if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        budget *= 0.35
        type_car = "Cabrio"
    elif season == "Winter":
        budget *= 0.65
        type_car = "Jeep"
elif 100 <= budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        budget *= 0.45
        type_car = "Cabrio"
    elif season == "Winter":
        budget *= 0.8
        type_car = "Jeep"
else:
    car_class = "Luxury class"
    type_car = "Jeep"
    budget *= 0.9

print(car_class)
print(f"{type_car} - {budget:.2f}")
