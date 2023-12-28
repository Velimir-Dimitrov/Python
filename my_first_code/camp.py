#camp_stuff = "tent, sleeping bags, water, raspberry pi, coffee, knife, ethernet cable, flash drive, beard oil, marshmallows"

#print(camp_stuff)

#PYTHON LIST

supplies = ["tent", "sleeping bags", "water", "raspberry pie", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]

camp_site = ["Crystal Lake", 404, 95.5, 10, False]

#supplies.append("toilet paper")
#supplies.append("bidet")
#supplies.extend(["toilet paper", "bidet"])
#supplies = supplies + ["toilet paper", "bidet"]
#supplies.insert(4, "bidet")
#supplies.insert("toilet paper")

#supplies.clear()
#supplies.remove("sleeping bags")

print("This item was just deleted: " + supplies.pop(0))
supplies.pop(0)
print(supplies)
