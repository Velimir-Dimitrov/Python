import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Student


# Run and print your queries
def add_students():
    Student.objects.create(
        student_id="FC5204",
        first_name="John",
        last_name="Doe",
        birth_date="1995-05-15",
        email="john.doe@university.com"
    )

    student = Student(
        student_id="FE0054",
        first_name="Jane",
        last_name="Smith",
        email="jane.smith@university.com"
    )
    student.save()

    another_student = Student()
    another_student.student_id = "FH2014"
    another_student.first_name = "Alice"
    another_student.last_name = "Johnson"
    another_student.birth_date = "1998-02-10"
    another_student.email = "alice.johnson@university.com"
    another_student.save()

    Student.objects.create(
        student_id="FH2015",
        first_name="Bob",
        last_name="Wilson",
        birth_date="1996-11-25",
        email="bob.wilson@university.com"
    )


# Test code
# add_students()
# print(Student.objects.all())

def get_students_info():
    result = []
    for record in Student.objects.all():
        result.append(f"Student №{record.student_id}: {record.first_name} {record.last_name}; Email: {record.email}")
    return "\n".join(result)

# Test code
# print(get_students_info())


def update_students_emails():
    students = Student.objects.all()
    for record in students:
        record.email = record.email.replace(record.email.split("@")[1], "uni-students.com")
    Student.objects.bulk_update(students, ["email"])

# Test code
# update_students_emails()
# for student in Student.objects.all():
#     print(student.email)


def truncate_students():
    Student.objects.all().delete()

# Test code
# truncate_students()
# print(Student.objects.all())
# print(f"Number of students: {Student.objects.count()}")
