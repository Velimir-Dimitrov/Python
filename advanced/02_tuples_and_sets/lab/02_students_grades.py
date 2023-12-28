number_of_students = int(input())
student_record = {}

for student in range(number_of_students):
    student_name, student_grade = input().split()
    if student_name not in student_record:
        student_record[student_name] = []
    student_record[student_name].append(float(student_grade))

for name, grades in student_record.items():
    total_student_grades = [x for x in student_record[name]]
    average_grade = sum(total_student_grades)/len(total_student_grades)
    print(f"{name} -> {' '.join([f'{x:.2f}' for x in grades])} (avg: {average_grade:.2f})")