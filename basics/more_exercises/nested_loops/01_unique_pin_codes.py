import math
n1 = int(input())
n2 = int(input())
n3 = int(input())

for y in range(2, n1 + 1, 2):
    for z in range(2, n2 + 1):
        is_prime = True

        for i in range(2, int(math.sqrt(z)+1)):
            if z % i == 0:
                is_prime = False
                break
        if is_prime:
            for x in range(2, n3 + 1, 2):
                print(f'{y} {z} {x}')

