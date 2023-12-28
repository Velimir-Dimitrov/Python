n = int(input())

total = 0
musa = 0
mon = 0
kili = 0
k2 = 0
everest = 0

for _ in range(n):
    people_per_groups = int(input())
    total += people_per_groups
    if people_per_groups <= 5:
        musa += people_per_groups
    elif people_per_groups <= 12:
        mon += people_per_groups
    elif people_per_groups <= 25:
        kili += people_per_groups
    elif people_per_groups <= 40:
        k2 += people_per_groups
    elif 41 <= people_per_groups:
        everest += people_per_groups

percentage_musa = musa / total * 100
percentage_mon = mon / total * 100
percentage_kili = kili / total * 100
percentage_k2 = k2 / total * 100
percentage_everest = everest / total * 100

print(f'{percentage_musa:.2f}% \n{percentage_mon:.2f}% \n{percentage_kili:.2f}% \n{percentage_k2:.2f}% \n{percentage_everest:.2f}%')