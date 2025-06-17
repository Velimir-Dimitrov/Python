def gen_vector(list_of_num, index):
    if index == len(vector):
        print("".join([str(n) for n in list_of_num]))
        return

    for number in range(0,2):
        list_of_num[index] = number
        gen_vector(list_of_num, index + 1)


vector = [0 for _ in range(int(input()))]
gen_vector(vector, 0)

# # Inputs
# 3
# 5