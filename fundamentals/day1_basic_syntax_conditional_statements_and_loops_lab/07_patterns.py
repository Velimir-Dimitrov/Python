n = int(input())

for roll in range(n + 1):
    for colum in range(roll):
        print("*", end='')
    print()
for roll in range(n - 1, -1, -1):
    for colum in range(roll):
        print("*", end='')
    print()
