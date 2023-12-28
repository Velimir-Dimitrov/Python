def calculate_cost(order, quantity):
    result = 0
    if order == "coffee":
        result = 1.50 * quantity
    elif order == "water":
        result = 1.00 * quantity
    elif order == "coke":
        result = 1.40 * quantity
    elif order == "snacks":
        result = 2.00 * quantity
    return result


product = input()
amount = int(input())
total_cost = calculate_cost(product, amount)
print(f'{total_cost:.2f}')
