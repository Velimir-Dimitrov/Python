budget = float(input())
price_kg_flour = float(input())

price_eggs = price_kg_flour * 0.75
price_1l_milk = price_kg_flour * 1.25

loaf_bread = price_eggs + (price_1l_milk / 4) + price_kg_flour
colored_eggs = 0
loaf_bread_counter = 0

while budget > loaf_bread:
    budget -= loaf_bread
    loaf_bread_counter += 1
    colored_eggs += 3
    if loaf_bread_counter % 3 == 0:
        colored_eggs -= loaf_bread_counter - 2
print(f"You made {loaf_bread_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
