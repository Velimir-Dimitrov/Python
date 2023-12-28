import os

WORKING_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(WORKING_DIR, 'numbers.txt')
total_sum = 0
file = open(file_path, 'r')
# for line in range(1, 6):
#     file.write(f"{line}\n")

numbers = file.read().replace('\n', ' ').strip()
for number in numbers.split():
    total_sum += int(number)
print(total_sum)

file.close()