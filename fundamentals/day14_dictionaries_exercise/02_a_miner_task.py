command = input()
miner_dict = {}

while command != "stop":
    resource = command
    quantity = int(input())
    if resource not in miner_dict.keys():
        miner_dict[resource] = 0
    miner_dict[resource] += quantity
    command = input()
[(print(f'{resource} -> {quantity}')) for resource, quantity in miner_dict.items()]


