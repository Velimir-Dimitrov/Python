names_of_the_gifts = input().split()
while True:
    command = input().split()
    if command[0] == "No" and command[1] == "Money":
        break
    if "OutOfStock" in command:
        for index in range(len(names_of_the_gifts)):
            if names_of_the_gifts[index] == command[1]:
                names_of_the_gifts[index] = "None"
    elif "Required" in command:
        if len(names_of_the_gifts) > int(command[2]) >= 0:
            names_of_the_gifts[int(command[2])] = command[1]
    elif "JustInCase" in command:
        names_of_the_gifts[-1] = command[1]
print(' '.join(str(el) for el in names_of_the_gifts if el != "None"))