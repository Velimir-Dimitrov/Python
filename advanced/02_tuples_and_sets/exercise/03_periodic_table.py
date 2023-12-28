number_of_lines = int(input())
unique_chemical_compounds = set()

for line in range(number_of_lines):
    compounds = input().split()
    while compounds:
        unique_chemical_compounds.add(compounds.pop())
print(*unique_chemical_compounds, sep="\n")
