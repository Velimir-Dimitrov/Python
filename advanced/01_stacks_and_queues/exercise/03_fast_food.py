from collections import deque

quantity_of_food = int(input())
food_orders = deque([int(el) for el in input().split()])

print(max(food_orders))

while food_orders and quantity_of_food:
    if food_orders[0] > quantity_of_food:
        print("Orders left:", end=" ")
        print(*food_orders, sep=" ")
        break
    quantity_of_food -= food_orders.popleft()
else:
    print("Orders complete")