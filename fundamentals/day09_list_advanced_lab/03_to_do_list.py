def to_do(some_list):
    to_do_list = []
    command = input()

    while command != "End":
        to_do_list.append(command)
        command = input()
    to_do_list.sort(key=lambda x: int(x.split('-')[0]))
    result = [note.split("-")[1] for note in to_do_list]
    return result


print(to_do(list))

