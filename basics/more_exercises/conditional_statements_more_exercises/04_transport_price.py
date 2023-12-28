distance = int(input())
time = input()
taxi = 0.70
bus = 0.09
train = 0.06
cost = 0

if distance < 20:
    if time == "day":
        cost = taxi + distance * 0.79
    elif time == "night":
        cost = taxi + distance * 0.90
elif 20 <= distance < 100:
    cost = distance * bus
else:
    cost = distance * train

print(f'{cost:.2f}')

