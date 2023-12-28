men_clients = int(input())
women_clients = int(input())
number_tables = int(input())

for man in range(1, men_clients + 1):
    for woman in range(1, women_clients + 1):
        number_tables -= 1
        if number_tables >= 0:
            print(f'({man} <-> {woman})', end = ' ')
        else:
            break