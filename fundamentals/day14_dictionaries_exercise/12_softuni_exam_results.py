students_dict = {}
course_dict = {}

while True:
    command = input()
    if command == "exam finished":
        break
    if "banned" in command:
        name = command.split("-")[0]
        students_dict.pop(name)
        continue
    student, course, points = command.split("-")
    points = int(points)
    if student not in students_dict:
        students_dict[student] = {}
    if course not in students_dict[student]:
        students_dict[student][course] = 0
    if students_dict[student][course] < points:
        students_dict[student][course] = points
    if course not in course_dict.keys():
        course_dict[course] = 0
    course_dict[course] += 1

print("Results:")
for name, courses in students_dict.items():
    for course, points in students_dict[name].items():
        print(f"{name} | {points}")
print("Submissions:")
for course, students in course_dict.items():
    print(f"{course} - {students}")
