number_of_lines = int(input())
list_of_numbers = []
for line in range(number_of_lines):
    current_number = int(input())
    list_of_numbers.append(current_number)
command = input()

for index in range(len(list_of_numbers) - 1, -1, -1):
    element = list_of_numbers[index]
    if command == "even" and element % 2 != 0:
        list_of_numbers.remove(element)
    elif command == "odd" and element % 2 == 0:
        list_of_numbers.remove(element)
    elif command == "negative" and element >= 0:
        list_of_numbers.remove(element)
    elif command == "positive" and element < 0:
        list_of_numbers.remove(element)
print(list_of_numbers)
