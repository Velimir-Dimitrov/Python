factor_num = int(input())
count_num = int(input())
new_num = 0
num_list = []

while count_num > 0:
    new_num += factor_num
    num_list.append(new_num)
    count_num -= 1
print(num_list)