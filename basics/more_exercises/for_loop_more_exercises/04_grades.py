number_of_students = int(input())

top = 0
around_4 = 0
around_3 = 0
fail = 0
total = 0

for students in range(1, number_of_students + 1):
    exam_grade = float(input())
    total += exam_grade
    if exam_grade < 3:
        fail += 1
    elif 4 > exam_grade >= 3:
        around_3 += 1
    elif 5 > exam_grade >= 4:
        around_4 += 1
    else:
        top += 1

average = total / number_of_students

top_percentage = top / number_of_students * 100
around_4_percentage = around_4 / number_of_students * 100
around_3_percentage = around_3 / number_of_students * 100
fail_percentage = fail / number_of_students * 100

print(f"Top students: {top_percentage:.2f}%")
print(f"Between 4.00 and 4.99: {around_4_percentage:.2f}%")
print(f"Between 3.00 and 3.99: {around_3_percentage:.2f}%")
print(f"Fail: {fail_percentage:.2f}%")
print(f"Average: {average:.2f}")

