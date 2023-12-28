farmed_materials = input().lower().split(" ")
legendary_mats = ["shards", "fragments", "motes"]
starting_quantity = 0
total_materials = dict.fromkeys(legendary_mats, starting_quantity)
sufficient_mats = False

while True:
    for element in range(0, len(farmed_materials), 2):
        quantity = int(farmed_materials[element])
        material = farmed_materials[element + 1]
        if material not in total_materials.keys():
            total_materials[material] = 0
        total_materials[material] += quantity
        if total_materials["shards"] >= 250:
            total_materials["shards"] -= 250
            print("Shadowmourne obtained!")
            sufficient_mats = True
            break
        elif total_materials["fragments"] >= 250:
            total_materials["fragments"] -= 250
            print("Valanyr obtained!")
            sufficient_mats = True
            break
        elif total_materials["motes"] >= 250:
            total_materials["motes"] -= 250
            print("Dragonwrath obtained!")
            sufficient_mats = True
            break
    if sufficient_mats:
        break
    farmed_materials = input().lower().split(" ")
[(print(f"{material}: {quantity}")) for material, quantity in total_materials.items()]