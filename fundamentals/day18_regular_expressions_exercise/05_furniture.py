import re

command = input()
pattern = r"\b([A-Za-z_]+)<<([0]|[1-9][0-9]*\.?\d+?)!([1-9]+\d?)\b"
bought_furniture = []
total_cost = 0
while command != "Purchase":
    current_furniture = re.search(pattern, command)
    if current_furniture:
        furniture_name, price, quantity = current_furniture.groups()
        bought_furniture.append(furniture_name)
        total_cost += float(price) * int(quantity)
    command = input()
print(f"Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")
