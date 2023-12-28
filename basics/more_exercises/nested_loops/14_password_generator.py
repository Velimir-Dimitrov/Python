n = int(input())
l = int(input())
c = 97 + l

for s1 in range(1, n):
    for s2 in range(1, n):
        for s3 in range(97, c):
            for s4 in range(97, c):
                for s5 in range(1, n + 1):
                    if s5 > s1 and s5 > s2:
                        print(f'{s1}{s2}{chr(s3)}{chr(s4)}{s5}', end = " ")