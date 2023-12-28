start_range = int(input())
end_range = int(input())
magic_number = int(input())

combination_number = 0
flag = False

for x in range(start_range,end_range + 1):
    for y in range(start_range, end_range + 1):
        combination_number += 1
        if x + y == magic_number:
            flag = True
            break
    if flag:
        break
if flag:
        print(f"Combination N:{combination_number} ({x} + {y} = {magic_number})")

else:
    print(f"{combination_number} combinations - neither equals {magic_number}")