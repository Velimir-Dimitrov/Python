rolls = int(input())
students_dict = {}

for pair in range(rolls):
    name = input()
    grade = float(input())
    if name not in students_dict:
        students_dict[name] = []
    students_dict[name].append(grade)

[(print(f"{name} -> {sum(grades)/len(grades):.2f}")) for name, grades in students_dict.items() if sum(grades)/len(grades) >= 4.5]
