days = int(input())
type_housing = input()
rate = input()
room_for_one_person, apartment, president_apartment = 18, 25, 35
discount, price, final_price = 0, 0, 0

if days >= 1:
    days -= 1

if type_housing == "room for one person":
    price = room_for_one_person * days
elif type_housing == "apartment":
    if days < 10:
        discount = 0.7
    elif 10 <= days <= 15:
        discount = 0.65
    elif days > 15:
        discount = 0.5
    price = apartment * discount * days
elif type_housing == "president apartment":
    if days < 10:
        discount = 0.9
    elif 10 <= days <= 15:
        discount = 0.85
    elif days > 15:
        discount = 0.8
    price = president_apartment * discount * days

if rate == "positive":
    final_price = price * 1.25
elif rate == "negative":
    final_price = price * 0.9

print(f'{final_price:.2f}')
