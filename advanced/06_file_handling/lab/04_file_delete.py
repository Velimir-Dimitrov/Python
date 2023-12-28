import os

WORKING_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(WORKING_DIR, 'my_first_file.txt')

try:
    os.remove(file_path)
except FileNotFoundError:
    print("File already deleted!")

