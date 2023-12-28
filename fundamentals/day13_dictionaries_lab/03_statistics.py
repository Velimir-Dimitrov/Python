command = input()
food_dict = {}

while ":" in command:
    key, value = command.split(": ")
    value = int(value)
    if key in food_dict:
        food_dict[key] += value
    else:
        food_dict[key] = value
    command = input()

print("Products in stock:")
[print(f"- {product}: {quantity}") for product, quantity in food_dict.items()]
print(f"Total Products: {len(food_dict)}")
print(f"Total Quantity: {sum(food_dict.values())}")