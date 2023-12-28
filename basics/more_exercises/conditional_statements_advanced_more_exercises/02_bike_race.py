number_juniors = int(input())
number_seniors = int(input())
type_track = input()

price_juniors = 0
price_seniors = 0

if type_track == "trail":
    price_juniors = 5.50
    price_seniors = 7

elif type_track == "cross-country":
    price_juniors = 8
    price_seniors = 9.5
    if (number_seniors + number_juniors) >= 50:
        price_juniors *= 0.75
        price_seniors *= 0.75
elif type_track == "downhill":
    price_juniors = 12.25
    price_seniors = 13.75

elif type_track == "road":
    price_juniors = 20
    price_seniors = 21.5

donation = (price_juniors * number_juniors + price_seniors * number_seniors) * 0.95

print(f'{donation:.2f}')

