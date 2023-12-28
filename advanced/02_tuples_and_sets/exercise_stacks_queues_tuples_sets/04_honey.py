from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar = deque([int(y) for y in input().split()])
symbols = deque(input().split())

total_honey = 0

while working_bees and nectar:
    current_bee = working_bees[0]
    current_nectar = nectar[-1]
    current_process = symbols[0]
    current_bee_honey = 0
    if current_bee > current_nectar:
        nectar.pop()
        continue
    else:
        if current_process == "+":
            current_bee_honey = abs(current_bee + current_nectar)
        elif current_process == "-":
            current_bee_honey = abs(current_bee - current_nectar)
        elif current_process == "*":
            current_bee_honey = abs(current_bee * current_nectar)
        elif current_process == "/" and current_nectar != 0:
            current_bee_honey = abs(current_bee / current_nectar)
        total_honey += current_bee_honey
    working_bees.popleft()
    nectar.pop()
    symbols.popleft()

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: ", end="")
    print(*working_bees,sep=", ")
if nectar:
    print(f"Nectar left: ", end="")
    print(*nectar, sep=", ")