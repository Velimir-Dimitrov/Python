start_number = int(input())
end_number = int(input())
magic_number = int(input())

counter = 0
found = False

for n1 in range(start_number, end_number + 1):
    for n2 in range(start_number, end_number + 1):
        counter += 1
        if n1 + n2 == magic_number:
            print(f'Combination N:{counter} ({n1} + {n2} = {magic_number})')
            found = True
            break
    if found:
        break
if not found:
    print(f"{counter} combinations - neither equals {magic_number}")
