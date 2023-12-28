number_fails = int(input())
command = input()

total_grades = 0
number_problems = 0
last_problem = ''
fail = 0

while True:
    grade = int(input())
    last_problem = command
    total_grades += grade
    number_problems += 1
    if grade <= 4:
        fail += 1

    if fail == number_fails:
        print(f"You need a break, {number_fails} poor grades.")
        break

    command = input()

    if command == "Enough":
        average_grade = total_grades / number_problems
        print(f"Average score: {average_grade:.2f}\nNumber of problems: {number_problems}\nLast problem: {last_problem}")
        break