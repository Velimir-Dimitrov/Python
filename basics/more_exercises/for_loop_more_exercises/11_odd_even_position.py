import sys
n = int(input())

odd_sum = 0
odd_max_num = -sys.maxsize
odd_min_num = sys.maxsize

even_sum = 0
even_max_num = -sys.maxsize
even_min_num = sys.maxsize

for i in range(1, n + 1):
    number = float(input())
    if i % 2 == 0:
        even_sum += number
        if even_max_num < number:
            even_max_num = number
        if even_min_num > number:
            even_min_num = number
    else:
        odd_sum += number
        if odd_max_num < number:
            odd_max_num = number
        if odd_min_num > number:
            odd_min_num = number

print(f"OddSum={odd_sum:.2f},")
if odd_min_num == sys.maxsize:
    print("OddMin=No,")
    print("OddMax=No,")
else:
    print(f"OddMin={odd_min_num:.2f},")
    print(f"OddMax={odd_max_num:.2f},")
print(f"EvenSum={even_sum:.2f},")
if even_min_num == sys.maxsize:
    print("EvenMin=No,")
    print("EvenMax=No")
else:
    print(f"EvenMin={even_min_num:.2f},")
    print(f"EvenMax={even_max_num:.2f}")