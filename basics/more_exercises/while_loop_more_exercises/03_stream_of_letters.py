command = ""
word = ""
total_word = ""
c_counter = 0
o_counter = 0
n_counter = 0

while command != "End":
    command = input()

    if command == "c" and c_counter == 0:
        c_counter += 1
    elif command == "o" and o_counter == 0:
        o_counter += 1
    elif command == "n" and n_counter == 0:
        n_counter += 1
    elif len(command) == 1:
        if 65 <= ord(command) <= 90 or 97 <= ord(command) <= 122:
            word += command

    if c_counter > 0 and o_counter > 0 and n_counter > 0:
        c_counter = 0
        o_counter = 0
        n_counter = 0
        total_word += word + " "
        word = ""

print(total_word)