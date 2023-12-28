chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

cost_chicken = chicken_menu * 10.35
cost_fish = fish_menu * 12.40
cost_vegetarian = vegetarian_menu * 8.15
cost_food = cost_fish + cost_vegetarian + cost_chicken
cost_desert = cost_food * 0.2
cost_delivery = 2.5

total_cost = cost_food + cost_desert + cost_delivery
print(total_cost)
