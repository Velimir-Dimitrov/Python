items = input().split("|")
initial_budget = float(input())
current_budget = initial_budget
france_train_ticket = 150
bought_items = []
markup = 1.4

for element in items:
    current_item = element.split("->")
    if current_item[0] == "Clothes" and float(current_item[1]) <= 50.00 or \
            current_item[0] == "Shoes" and float(current_item[1]) <= 35.00 or \
            current_item[0] == "Accessories" and float(current_item[1]) <= 20.50:
        if current_budget - float(current_item[1]) >= 0:
            current_budget -= float(current_item[1])
            bought_items.append(float(current_item[1]) * markup)

for element in bought_items:
    print(f"{element:.2f}", end=" ")
print()
end_budget = current_budget + sum(bought_items)
profit = end_budget - initial_budget
print(f'Profit: {profit:.2f}')
if france_train_ticket <= end_budget:
    print("Hello, France!")
else:
    print("Not enough money.")
