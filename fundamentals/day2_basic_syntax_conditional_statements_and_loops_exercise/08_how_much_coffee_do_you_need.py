coffee = 0

while True:
    command = input()
    word = command.lower()
    if command == "END":
        break
    elif word == "coding" or word == "dog" or word == "cat" or word == "movie":
        if command.islower():
            coffee += 1
        else:
            coffee += 2
    else:
        continue
if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)