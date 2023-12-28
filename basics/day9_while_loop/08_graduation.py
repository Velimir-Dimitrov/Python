name = input()
year = 0
total_grades = 0
fail = 0

while True:
    grade = float(input())

    if grade < 4:
        fail += 1

        if fail == 2:
            failed_year = year + 1
            print(f"{name} has been excluded at {failed_year} grade")
            break
        continue

    year += 1
    total_grades += grade

    if year == 12:
        avarage_grade = total_grades / 12
        print(f"{name} graduated. Average grade: {avarage_grade:.2f}")
        break





