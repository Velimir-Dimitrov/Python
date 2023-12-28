first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(y) for y in input().split())
number_of_lines = int(input())

for line in range(number_of_lines):
    command = input().split()
    if len(command) > 2:
        current_numbers = set([int(command[x]) for x in range(2, len(command))])
    if command[0] == "Add":
        if command[1] == "First":
            first_sequence.update(current_numbers)
        elif command[1] == "Second":
            second_sequence.update(current_numbers)
    elif command[0] == "Remove":
        if command[1] == "First":
            first_sequence.difference_update(current_numbers)
        elif command[1] == "Second":
            for num in current_numbers:
                second_sequence.difference_update(current_numbers)
    elif command[0] == "Check":
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

sorted_first = sorted(first_sequence)
sorted_second = sorted(second_sequence)
print(', '.join([str(x) for x in sorted_first]))
print(', '.join([str(y) for y in sorted_second]))
