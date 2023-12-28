number = int(input())

for n1 in range(1, 10):
    if n1 >= number:
        break
    for n2 in range(1, 10):
        if n2 >= number:
            break
        for n3 in range(1, 10):
            if n3 >= number:
                break
            for n4 in range(1,10):
                if n4 >= number:
                    break
                if n1 + n2 == n3 + n4 and number % (n1 + n2) == 0:
                    print(f'{n1}{n2}{n3}{n4}', end = " ")