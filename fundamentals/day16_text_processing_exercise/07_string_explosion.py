string_with_explosions = input()
new_string = ""
index = 0
extra = 0

while string_with_explosions:
    explosion = 0
    explosion += extra
    extra = 0
    if string_with_explosions[index] == ">":
        explosion += int(string_with_explosions[index + 1])
        new_string += ">"
        string_with_explosions = string_with_explosions[index + 1::]
    if explosion == 1:
        string_with_explosions = string_with_explosions[index + 1::]
        continue
    elif explosion > 1:
        string_with_explosions = string_with_explosions[index + 1::]
        extra += explosion - 1
        continue
    new_string += string_with_explosions[index]
    string_with_explosions = string_with_explosions[index + 1::]
print(new_string)