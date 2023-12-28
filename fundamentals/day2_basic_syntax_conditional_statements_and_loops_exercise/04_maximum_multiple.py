divisor = int(input())
boundary = int(input())

for dupe in range(boundary, 1, -1):
    if dupe % divisor == 0:
        print(dupe)
        break

