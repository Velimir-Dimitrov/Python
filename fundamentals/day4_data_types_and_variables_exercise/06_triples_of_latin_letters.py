import string
n = int(input())
lower_case = string.ascii_lowercase

for letter1 in range(n):
    first_case = lower_case[letter1]
    for letter2 in range(n):
        second_case = lower_case[letter2]
        for letter3 in range(n):
            third_case = lower_case[letter3]
            print(f'{first_case}{second_case}{third_case}')
