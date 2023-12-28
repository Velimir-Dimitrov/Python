from collections import deque

total_litres_of_water = int(input())
waiting_people = deque()
name = input()

while name != "Start":
    waiting_people.append(name)
    name = input()

command = input()
while command != "End":
    if "refill" in command:
        refill_litres = int(command.split()[1])
        total_litres_of_water += refill_litres
    else:
        required_litres_of_water = int(command)
        current_person = waiting_people.popleft()
        if required_litres_of_water <= total_litres_of_water:
            total_litres_of_water -= required_litres_of_water
            print(f"{current_person} got water")
        else:
            print(f"{current_person} must wait")
    command = input()
print(f"{total_litres_of_water} liters left")