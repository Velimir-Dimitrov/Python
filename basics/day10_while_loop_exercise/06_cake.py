cake_width = int(input())
cake_length = int(input())

cake_total = cake_width * cake_length


while True:
    command = input()
    if command == "STOP":
        print(f'{cake_total} pieces are left.')
        break
    cake_total -= int(command)
    if cake_total < 0:
        print(f"No more cake left! You need {abs(cake_total)} pieces more.")
        break
