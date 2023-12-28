string_int = input().split(", ")
int_list = [int(el) for el in string_int]
for element in int_list:
    int_list.append(int_list.pop(int_list.index(0)))
print(int_list)
