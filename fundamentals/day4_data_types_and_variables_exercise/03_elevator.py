from math import ceil
n_people = int(input())
capacity = int(input())

courses = ceil(n_people / capacity)
print(courses)