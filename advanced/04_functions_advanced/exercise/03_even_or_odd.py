def even_odd(*args):
    command = args[-1]
    num_dict = {'even': [], 'odd': []}
    [num_dict['even'].append(int(el)) if int(el) % 2 == 0 else num_dict['odd'].append(int(el)) for el in args[0:-1]]

    return num_dict[command]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))