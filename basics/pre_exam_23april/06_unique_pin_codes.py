import math

n1 = int(input())
n2 = int(input())
n3 = int(input())

for a in range(2,n1 + 1):
    for b in range(2, n2 + 1):
        for i in range(2, int(math.sqrt(b) + 1)):
            if b % i == 0:
                break
        else:
            for c in range(2, n3 + 1):
                if a % 2 == 0 and c % 2 == 0:
                    print(f'{a} {b} {c}')