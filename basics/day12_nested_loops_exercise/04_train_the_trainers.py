n = int(input())
presentation = input()

grades_counter = 0
sum_grades = 0

while presentation != "Finish":
    grades = 0

    for _ in range(n):
        grades += float(input())
        grades_counter += 1
    print(f'{presentation} - {grades / n:.2f}.')

    sum_grades += grades
    presentation = input()

total_average = sum_grades / grades_counter
print(f"Student's final assessment is {total_average:.2f}.")