string_of_int = input()
beggars = int(input())

str_list = string_of_int.split(', ')
sum_list = []

while len(str_list) > 0:
    for index in range(beggars):
        if len(str_list) == 0:
            if len(sum_list) == beggars:
                break
            else:
                sum_list.insert(index, 0)
        elif len(sum_list) < beggars:
            sum_list.append(int(str_list[0]))
            str_list.pop(0)
        else:
            sum_list[index] += int(str_list[0])
            str_list.pop(0)
print(sum_list)
