from collections import deque

monsters_armor_values = deque(int(x) for x in input().split(','))
solder_striking_values = [int(x) for x in input().split(',')]
killed_monsters = 0

while monsters_armor_values and solder_striking_values:
    monster_armor = monsters_armor_values.popleft()
    soldier_strike = solder_striking_values.pop()
    if soldier_strike == monster_armor:
        killed_monsters += 1
        continue
    elif soldier_strike > monster_armor:
        killed_monsters += 1
        soldier_strike -= monster_armor
        if solder_striking_values:
            solder_striking_values[-1] += soldier_strike
        else:  # solder_striking_values is empty
            solder_striking_values.append(soldier_strike)

    elif soldier_strike < monster_armor:
        monster_armor -= soldier_strike
        monsters_armor_values.append(monster_armor)

if not monsters_armor_values:
    print("All monsters have been killed!")
if not solder_striking_values:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")
