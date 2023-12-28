plastic = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

cost_plastic = (plastic + 2) * 1.50
cost_paint = (paint + (paint *0.1)) * 14.50
cost_thinner = thinner * 5
cost_bags = 0.40
cost_products = cost_thinner + cost_paint + cost_plastic + cost_bags
cost_worker = (cost_products * 0.3) * hours
total_cost = cost_products + cost_worker
print(total_cost)

