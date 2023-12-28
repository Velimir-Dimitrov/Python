people_string = input().split()
k = int(input()) - 1

people_list = [int(el) for el in people_string]
temp_list_start = []
temp_list_end = []
kill_list = []

while len(kill_list) < len(people_string):
    temp_list_start.clear(), temp_list_end.clear()
    new_k = k
    if len(people_list) == 1:
        kill_list.append(people_list[0])
        break
    while len(people_list) <= new_k:
        new_k -= len(people_list)
    for person in range(len(people_list)):
        if person < new_k:
            temp_list_end.append(people_list[person])
        elif new_k == person:
            kill_list.append(people_list[person])
        else:
            temp_list_start.append(people_list[person])
    people_list.clear()
    people_list += temp_list_start
    people_list += temp_list_end
print('[' + ','.join([str(n) for n in kill_list]) + ']')