def replace(some_string, char, replacement):
    replaced_chars = some_string.replace(char, replacement)
    return replaced_chars


def string_check(some_string, checked_string):
    if checked_string in some_string:
        return True
    return False


def start_check(some_string, start_string):
    end_index = len(start_string)
    sliced_start = some_string[:end_index]
    if sliced_start == start_string:
        return True
    return False


def make_lower(some_string):
    return some_string.lower()


def find_last_index(some_string, some_char):
    last_index = some_string.rfind(some_char)
    return last_index


def removing_part(some_string, some_index, count_num):
    starting_index = int(some_index)
    count_num = int(count_num)
    sliced_start = some_string[:starting_index]
    end_index = starting_index + count_num
    sliced_end = some_string[end_index:]
    new_string = sliced_start + sliced_end
    return new_string


received_string = input()
command = input()

while command != "End":
    command = command.split(" ")
    if command[0] == "Translate":
        current_command, current_char, current_replacement = command
        received_string = replace(received_string, current_char, current_replacement)
        print(received_string)
    elif command[0] == "Includes":
        current_command, sting_for_check = command
        print(string_check(received_string, sting_for_check))
    elif command[0] == "Start":
        current_command, substring_for_check = command
        print(start_check(received_string, substring_for_check))
    elif command[0] == "Lowercase":
        received_string = received_string.lower()
        print(received_string)
    elif command[0] == "FindIndex":
        current_command, searched_char = command
        print(find_last_index(received_string, searched_char))
    elif command[0] == "Remove":
        current_command, start_index, count = command
        received_string = removing_part(received_string, start_index, count)
        print(received_string)
    command = input()


