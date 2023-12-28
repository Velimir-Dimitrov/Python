n = input()
my_list = []

for char in n:
    my_list.append(char)
my_list.sort(reverse=True)
print(''.join(my_list))