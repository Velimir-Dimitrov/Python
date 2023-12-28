food_type = input().split()
food_info_dic = dict()

for i in range(0, len(food_type), 2):
    food_info_dic[food_type[i]] = int(food_type[(i + 1)])
print(food_info_dic)