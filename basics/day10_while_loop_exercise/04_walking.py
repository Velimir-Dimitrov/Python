total = 0
GOAL = 10000
command = ''

while True:
    steps = input()
    if steps == "Going home":
        command = "home"
        continue
    total += int(steps)
    diff = abs(total - GOAL)
    if total >= GOAL:
        print(f"Goal reached! Good job!\n{diff} steps over the goal!")
        break
    if command == "home" and total < GOAL:
        print(f'{diff} more steps to reach goal.')
        break
