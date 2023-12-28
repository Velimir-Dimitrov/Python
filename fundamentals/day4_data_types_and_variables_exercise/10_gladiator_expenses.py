lost_count = int(input())
helmet_repair_price = float(input())
sword_repair_price = float(input())
shield_repair_price = float(input())
armor_repair_price = float(input())
total_expenses = 0
broken_shield_counter = 0

for lost in range(1, lost_count + 1):
    if lost % 2 == 0:
        total_expenses += helmet_repair_price
    if lost % 3 == 0:
        total_expenses += sword_repair_price
        if lost % 2 == 0:
            total_expenses += shield_repair_price
            broken_shield_counter += 1
            if broken_shield_counter % 2 == 0:
                total_expenses += armor_repair_price
print(f"Gladiator expenses: {total_expenses:.2f} aureus")

