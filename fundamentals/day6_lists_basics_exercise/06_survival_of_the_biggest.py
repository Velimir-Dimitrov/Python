string_of_numbers = input().split()
small_num_counter = int(input())
list_of_numbers = []
final_numbers = []

for element in string_of_numbers:
    list_of_numbers.append(int(element))
final_numbers += list_of_numbers
list_of_numbers.sort()

for removal in range(small_num_counter):
    final_numbers.remove(list_of_numbers[0])
    list_of_numbers.pop(0)

print(f"{', '.join([str(x) for x in final_numbers])}")

