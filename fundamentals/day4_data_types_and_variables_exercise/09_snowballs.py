number_of_snowballs = int(input())
snowball_value = 0
top_quality = 0
top_weight = 0
top_time = 0
top_value = 0

for _ in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight // snowball_time) ** snowball_quality
    if top_value < snowball_value:
        top_weight = snowball_weight
        top_time = snowball_time
        top_quality = snowball_quality
        top_value = snowball_value
print(f"{top_weight} : {top_time} = {top_value} ({top_quality})")


