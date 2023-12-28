def train_adjustment(command):
    command = command.split(" ")
    action = command[0]
    if action == "add":
        passengers = int(command[1])
        train_wagons[-1] += passengers
    elif action == "insert":
        passengers = int(command[-1])
        wagon_position = int(command[1])
        train_wagons[wagon_position] += passengers
    elif action == "leave":
        passengers = int(command[-1])
        wagon_position = int(command[1])
        train_wagons[wagon_position] -= passengers


train_wagons = [0 for x in range(int(input()))]
command = input()

while command != "End":
    train_adjustment(command)
    command = input()
print(train_wagons)

