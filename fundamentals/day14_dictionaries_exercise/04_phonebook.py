command = input()
phone_dict = {}

while not command.isnumeric():
    name, number = command.split("-")
    phone_dict[name] = number
    command = input()

n = int(command)

for line in range(n):
    name = input()
    if name in phone_dict.keys():
        print(f"{name} -> {phone_dict[name]}")
    else:
        print(f"Contact {name} does not exist.")


