cost_vegetables_per_kg = float(input())
cost_fruits_per_kg = float(input())
kg_vegetables = int(input())
kg_fruits = int(input())

cost_vegetables = cost_vegetables_per_kg * kg_vegetables
cost_fruits = cost_fruits_per_kg * kg_fruits
total_cost = (cost_vegetables + cost_fruits) / 1.94

print(f'{total_cost:.2f}')
