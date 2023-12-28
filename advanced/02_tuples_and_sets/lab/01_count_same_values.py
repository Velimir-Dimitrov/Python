numbers = tuple(float(x) for x in input().split())
checked = []

for number in numbers:
    if number not in checked:
        print(f"{number} - {numbers.count(number)} times")
        checked.append(number)

