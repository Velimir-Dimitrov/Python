import math
total_field_area = int(input())
grape_per_area = float(input())
required_litres_wine = int(input())
workers = int(input())

total_grape = total_field_area * grape_per_area
total_wine = total_grape * 0.4 / 2.5


diff = abs(total_wine - required_litres_wine)
wine_per_worker = diff / workers

if total_wine < required_litres_wine:
    print(f'It will be a tough winter! More {math.floor(diff)} liters wine needed.')
elif total_wine >= required_litres_wine:
    print(f'Good harvest this year! Total wine: {math.floor(total_wine)} liters.')
    print(f"{math.ceil(diff)} liters left -> {math.ceil(wine_per_worker)} liters per person.")
