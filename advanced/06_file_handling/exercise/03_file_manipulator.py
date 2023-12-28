import os


def create(file):
    with open(file, 'w') as f:
        return


def add_to(file, content):
    with open(file, 'a') as f:
        f.write(content + '\n')


def replace_in(file, old_string, new_string):
    try:
        with open(file, 'r') as f:
            file_text = f.read()
        with open(file, 'w') as f:
            if old_string in file_text:
                file_text = file_text.replace(old_string, new_string)
            f.write(file_text)
    except FileNotFoundError:
        return print("An error occurred")


def delete(file):
    try:
        os.remove(file)
    except FileNotFoundError:
        return print("An error occurred")


commands = {'Create': create, 'Add': add_to, 'Replace': replace_in, 'Delete': delete}

command = input()

while command != "End":
    action, file_name, *file_content = command.split('-')
    commands[action](file_name, *file_content)
    command = input()


