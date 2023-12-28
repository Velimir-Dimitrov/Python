import os

WORKING_DIR = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(WORKING_DIR, 'my_first_file.txt')
file = open(file_path, 'w')
file.write("I just created my first file!")
file.close()
