n = int(input())

total = 0

for i in range(0, n):
    total += int(input())
print(f'{total / n:.2f}')