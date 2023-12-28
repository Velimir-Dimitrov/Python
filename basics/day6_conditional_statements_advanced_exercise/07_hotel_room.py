month = input()
days = int(input())

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    rent_studio = studio * days
    rent_apartment = apartment * days
    if 7 < days <= 14:
        rent_studio = rent_studio - (rent_studio * 0.05)
    elif days > 14:
        rent_studio = rent_studio - (rent_studio * 0.3)
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    rent_studio = studio * days
    rent_apartment = apartment * days
    if days > 14:
        rent_studio = rent_studio - (rent_studio * 0.2)

elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    rent_studio = studio * days
    rent_apartment = apartment * days

if days > 14:
    rent_apartment = rent_apartment - (rent_apartment * 0.1)

print(f"Apartment: {rent_apartment:.2f} lv.")
print(f"Studio: {rent_studio:.2f} lv.")
