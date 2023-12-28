paper_roll = int(input())
fabric_roll = int(input())
glue_litres = float(input())
discount = int(input())

paper_cost = paper_roll * 5.8
fabric_cost = fabric_roll * 7.2
glue_cost = glue_litres * 1.2

total_cost = paper_cost + fabric_cost + glue_cost
after_discount = total_cost - (total_cost * discount / 100)

print(f'{after_discount:.3f}')