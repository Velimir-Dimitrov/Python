from collections import deque

boxes_with_materials = [int(x) for x in input().split()]
magic_values = deque([int(y) for y in input().split()])

points = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
presents = {}

while boxes_with_materials and magic_values:
    current_material = boxes_with_materials[-1]
    current_magic = magic_values[0]

    if current_material == 0 and current_magic == 0:
        boxes_with_materials.pop()
        magic_values.popleft()
        continue
    if current_material == 0:
        boxes_with_materials.pop()
        continue
    if current_magic == 0:
        magic_values.popleft()
        continue

    total_magic = current_magic * current_material
    if total_magic > 0:
        boxes_with_materials.pop()
        magic_values.popleft()
        if total_magic in points:
            new_present = points[total_magic]
            if new_present not in presents:
                presents[new_present] = 0
            presents[new_present] += 1
        else:
            boxes_with_materials.append(current_material + 15)
    else:
        boxes_with_materials.append(boxes_with_materials.pop() + magic_values.popleft())

if ("Doll" in presents and "Wooden" in presents) or ("Teddy bear" in presents and "Bicycle" in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if boxes_with_materials:
    print(f"Materials left: {', '.join(str(x) for x in boxes_with_materials[::-1])}")
if magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")
for toy_name1,amount in sorted(presents.items()):
    print(f"{toy_name1}: {amount}")