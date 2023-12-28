season = input()
students = input()
number_of_students = int(input())
number_of_overnight = int(input())

price_per_overnight = 0
type_sport = ''

if season == "Winter":
    if students == "boys" or students == "girls":
        price_per_overnight = 9.6
        if students == "boys":
            type_sport = "Judo"
        elif students == "girls":
            type_sport = "Gymnastics"
    elif students == "mixed":
        type_sport = "Ski"
        price_per_overnight = 10
elif season == "Spring":
    if students == "boys" or students == "girls":
        price_per_overnight = 7.2
        if students == "boys":
            type_sport = "Tennis"
        elif students == "girls":
            type_sport = "Athletics"
    elif students == "mixed":
        type_sport = "Cycling"
        price_per_overnight = 9.5
elif season == "Summer":
    if students == "boys" or students == "girls":
        price_per_overnight = 15
        if students == "boys":
            type_sport = "Football"
        elif students == "girls":
            type_sport = "Volleyball"
    elif students == "mixed":
        type_sport = "Swimming"
        price_per_overnight = 20

total_price = price_per_overnight * number_of_overnight * number_of_students

if number_of_students >= 50:
    total_price *= 0.50
elif 20 <= number_of_students < 50:
    total_price *= 0.85
elif 10 <= number_of_students < 20:
    total_price *= 0.95

print(f"{type_sport} {total_price:.2f} lv.")
