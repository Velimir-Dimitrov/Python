import math
days = int(input())
food_left = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food= float(input()) / 1000

required_food = days * (dog_food + cat_food + turtle_food)
diff = abs(food_left - required_food)

if required_food <= food_left:
    print(f'{math.floor(diff)} kilos of food left.')
elif required_food > food_left:
    print(f'{math.ceil(diff)} more kilos of food are needed.')
    