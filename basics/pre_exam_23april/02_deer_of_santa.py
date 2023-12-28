from math import ceil,floor

days_traveling = int(input())
left_food = int(input())
food_per_day_deer1 = float(input())
food_per_day_deer2 = float(input())
food_per_day_deer3 = float(input())

needed_food_for_deer1 = days_traveling * food_per_day_deer1
needed_food_for_deer2 = days_traveling * food_per_day_deer2
needed_food_for_deer3 = days_traveling * food_per_day_deer3

total_food_needed = needed_food_for_deer3 + needed_food_for_deer2 + needed_food_for_deer1
diff = abs(left_food - total_food_needed)

if total_food_needed <= left_food:
    print(f'{floor(diff)} kilos of food left.')
else:
    print(f'{ceil(diff)} more kilos of food are needed.')