from collections import deque
chocolate = deque(int(x) for x in input().split(", "))
cups_of_milk = deque(int(y) for y in input().split(", "))
milkshakes = 0

while milkshakes != 5 and chocolate and cups_of_milk:
    if chocolate[-1] <= 0 and cups_of_milk[0] <= 0:
        chocolate.pop()
        cups_of_milk.popleft()
        continue
    if chocolate[-1] <= 0:
        chocolate.pop()
        continue
    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue
    if chocolate[-1] == cups_of_milk[0]:
        chocolate.pop()
        cups_of_milk.popleft()
        milkshakes += 1
    else:
        chocolate[-1] -= 5
        cups_of_milk.append(cups_of_milk.popleft())

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
print(f"Chocolate: {', '.join([str(x) for x in chocolate]) if chocolate else 'empty'}")
print(f"Milk: {', '.join(str(y) for y in cups_of_milk) if cups_of_milk else 'empty'}")
