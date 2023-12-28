number = int(input())
for i in range(2, int(number/2) + 1):
    if (number % i) == 0:
        print(False)
        break
else:
    print(True)

