number_a = int(input())
number_b = int(input())
max_num_passwords = int(input())

counter = 0
A = 35
B = 64

for x in range(1, number_a + 1):
    for y in range(1, number_b + 1):
        counter += 1
        if A == 56:
            A = 35
        if B == 97:
            B = 64
        print(f'{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}', end="|")
        A += 1
        B += 1
        if counter == max_num_passwords:
            break
    if counter == max_num_passwords:
        break



