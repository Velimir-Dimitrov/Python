list_food = input().split(" ")
dict_food = {}

for index in range(0, len(list_food), 2):
    dict_food[list_food[index]] = int(list_food[index + 1])

check_food = input().split(" ")

for food in check_food:
    if food in dict_food:
        print(f"We have {dict_food[food]} of {food} left")
    else:
        print(f"Sorry, we don't have {food}")
