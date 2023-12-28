import math

n1 = int(input())
n2 = int(input())
n3 = int(input())

for A in range(2, n1 + 1):
    if A % 2 != 0:
        continue
    for B in range(2, n2 + 1):
        for x in range(2, int(math.sqrt(B)) + 1):
            if B % x == 0:
                break
        else:
            for C in range(2, n3 + 1):
                if C % 2 == 0:
                    print(f'{A} {B} {C}')