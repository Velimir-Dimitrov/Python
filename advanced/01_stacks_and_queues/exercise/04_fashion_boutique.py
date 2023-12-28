clothes_in_the_box = [int(x) for x in input().split()]
rack_capacity = int(input())
number_of_racks = 0

while clothes_in_the_box:
    current_capacity = rack_capacity
    while clothes_in_the_box and clothes_in_the_box[-1] <= current_capacity:
        current_capacity -= clothes_in_the_box.pop()
    number_of_racks += 1
print(number_of_racks)
