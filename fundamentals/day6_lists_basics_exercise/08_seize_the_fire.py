fire_cells = input().split("#")
water = int(input())
extinguished_fires = []
effort = 0
total_fire = 0

for cell in fire_cells:
    '='.join(cell)
    single_fire = cell.split(" = ")
    if single_fire[0] == "High" and 81 <= int(single_fire[1]) <= 125 or \
            single_fire[0] == "Medium" and 51 <= int(single_fire[1]) <= 80 or \
            single_fire[0] == "Low" and 1 <= int(single_fire[1]) <= 50:
        if water - int(single_fire[1]) >= 0:
            water -= int(single_fire[1])
            extinguished_fires.append(int(single_fire[1]))
            effort += int(single_fire[1]) * 0.25
            total_fire += int(single_fire[1])
print("Cells:")
for extinguished_fire in extinguished_fires:
    print(f"- {extinguished_fire}")
print(f"Effort: {effort:.2f}")
print(f'Total Fire: {total_fire}')
