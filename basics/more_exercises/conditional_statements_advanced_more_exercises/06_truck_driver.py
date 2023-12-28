season = input()
distance = float(input())

price_per_km = 0
taxes = 0.9

if distance <= 5000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.75
    elif season == "Summer":
        price_per_km = 0.9
    elif season == "Winter":
        price_per_km = 1.05
elif 5000 < distance <= 10000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.95
    elif season == "Summer":
        price_per_km = 1.1
    elif season == "Winter":
        price_per_km = 1.25
elif 10000 < distance <= 20000:
    price_per_km = 1.45

profit = (price_per_km * distance) * 4
print(f'{profit * taxes:.2f}')
