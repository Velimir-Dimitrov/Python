electrons = int(input())
filled_shells = []
number_of_shells = 1

while electrons > 0:
    currently_filled = 0
    max_shell = (number_of_shells ** 2) * 2
    for position in range(1, 3):
        current_shell = number_of_shells ** 2
        if electrons >= current_shell and max_shell > 0:
            currently_filled += current_shell
            electrons -= current_shell
            max_shell -= 1
        else:
            currently_filled += electrons
            electrons = 0
            break
    filled_shells.append(currently_filled)
    number_of_shells += 1
print(filled_shells)
