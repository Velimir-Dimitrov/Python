command = input()
students_dict = {}

while ":" in command:
    student_name, student_id, course = command.split(":")
    if course not in students_dict:
        students_dict[course] = {student_name: student_id}

    else:
        students_dict[course][student_name] = student_id
    command = input()

command = command.replace("_", " ")

for student_name, student_id in students_dict[command].items():
    print(f"{student_name} - {student_id}")
