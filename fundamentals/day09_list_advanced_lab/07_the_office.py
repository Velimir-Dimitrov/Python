employees_happiness = list(map(int, (input().split())))
improvement_factor = int(input())
improved_happiness = list(map(lambda x: x * improvement_factor, employees_happiness))
employees_count = len(employees_happiness)
average_happiness = sum(improved_happiness) // employees_count
employees_happy = list(filter(lambda x: x > average_happiness, improved_happiness))
happy_count = len(employees_happy)

if happy_count >= employees_count//2:
    print(f'Score: {happy_count}/{employees_count}. Employees are happy!')
else:
    print(f"Score: {happy_count}/{employees_count}. Employees are not happy!")
