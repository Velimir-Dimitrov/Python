import math

n1= int(input())
d1 = int(input())
n2 = int(input())
d2 = int(input())

n_end = n1 + n2 + 1
d_end = d1 + d2 + 1
for x in range(n1, n_end):
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            break
    else:
        for y in range(d1, d_end):
            for c in range(2, int(math.sqrt(y) + 1)):
                if y % c == 0:
                    break
            else:
                print(f'{x}{y}')