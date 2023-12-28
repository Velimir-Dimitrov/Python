letter1 = input()
letter2 = input()
letter3 = input()

code1 = ord(letter1)
code2 = ord(letter2)
code3 = ord(letter3)
counter = 0

for x in range(code1, code2 + 1):
    if x == code3:
        continue
    for y in range(code1, code2 + 1):
        if y == code3:
            continue
        for i in range(code1, code2 + 1):
            if i == code3:
                continue
            counter += 1
            print(f'{chr(x)}{chr(y)}{chr(i)}', end = " ")
print(counter)