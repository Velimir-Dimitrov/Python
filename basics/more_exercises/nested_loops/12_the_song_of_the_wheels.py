control_num = int(input())
counter = 0
password = 1234
found_flag = False

for a in range(1,10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1,10):
                if a * b + c * d == control_num and a < b and c > d:
                    counter += 1
                    print(f'{a}{b}{c}{d}', end = " ")
                    if counter == 4:
                        password = f'{a}{b}{c}{d}'
                        found_flag = True
print()
if found_flag:
    print(f'Password: {password}')
else:
    print("No!")