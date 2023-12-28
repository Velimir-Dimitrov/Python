command = input()
courses_dict = {}

while command != "end":
    course_name, student_name = command.split(" : ")
    if course_name not in courses_dict:
        courses_dict[course_name] = []
    courses_dict[course_name].append(student_name)
    command = input()
for course,students in courses_dict.items():
    print(f"{course}: {len(students)}")
    for student in courses_dict[course]:
        print(f"-- {student}")