number_of_names = int(input())
list_of_names = []

for _ in range(number_of_names):
    name = input()
    list_of_names.append(name)
unique_names = set(list_of_names)
[print(name) for name in unique_names]