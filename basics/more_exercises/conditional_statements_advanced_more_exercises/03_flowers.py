num_chrysanthemum = int(input())
num_rose = int(input())
num_tulip = int(input())
season = input()
holiday = input()

price_bouquet = 2
price_chrysanthemum = 0
price_rose = 0
price_tulip = 0

if season == "Spring" or season == "Summer":
    price_chrysanthemum = 2
    price_rose = 4.1
    price_tulip = 2.5
elif season == "Autumn" or season == "Winter":
    price_chrysanthemum = 3.75
    price_rose = 4.50
    price_tulip = 4.15

total_price = num_chrysanthemum * price_chrysanthemum + num_rose * price_rose + num_tulip * price_tulip

if holiday == "Y":
    total_price *= 1.15
if season == "Spring" and num_tulip > 7:
    total_price *= 0.95
if season == "Winter" and num_rose >= 10:
    total_price *= 0.90
if num_tulip + num_chrysanthemum + num_rose > 20:
    total_price *= 0.80

print(f'{total_price + price_bouquet:.2f}')


