from collections import deque
from collections import defaultdict

tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while True:
    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break
    if not tools or not substances:
        print("Harry is lost in the temple. Oblivion awaits him.")
        break
    current_tool = tools.popleft()
    current_substance = substances.pop()
    current_result = current_substance * current_tool
    if current_result in challenges:
        challenges.remove(current_result)
    else:
        tools.append(current_tool + 1)
        if current_substance > 1:
            substances.append(current_substance - 1)
if substances:
    print(f"Substances: {', '.join([str(x) for x in substances])}")
if tools:
    print(f"Tools: {', '.join([str(x) for x in tools])}")
if challenges:
    print(f"Challenges: {', '.join([str(x) for x in challenges])}")



