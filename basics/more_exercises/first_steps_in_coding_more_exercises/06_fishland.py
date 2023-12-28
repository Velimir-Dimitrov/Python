mackerel_cost_per_kg = float(input())
sprat_cost_per_kg = float(input())
bonito_kg = float(input())
scad_kg = float(input())
clam_kg = int(input())

bonito_cost_per_kg = mackerel_cost_per_kg + (mackerel_cost_per_kg * 0.6)
total_bonito_cost = bonito_cost_per_kg * bonito_kg

scad_cost_per_kg = sprat_cost_per_kg + (sprat_cost_per_kg * 0.8)
total_scad_cost =  scad_cost_per_kg * scad_kg

total_clam_cost = clam_kg * 7.50

total_cost = total_clam_cost + total_scad_cost + total_bonito_cost
print(f'{total_cost:.2f}')
