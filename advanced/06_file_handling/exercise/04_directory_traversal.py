import os

directory = os.path.dirname(os.path.abspath(__file__))
result = {}

for path in os.listdir(directory):
    file = os.path.join(directory, path)
    if os.path.isfile(file):
        ext = path.split('.')[-1]
        if ext not in result:
            result[ext] = []
        result[ext].append(path)
    else:
        for el in os.listdir(file):
            filename = os.path.join(file)
            if os.path.isfile(filename):
                ext = el.split('')[-1]
                if ext not in result:
                    result[ext] = []
                result[ext].append(el)

with open(os.path.join(directory, 'report.txt'), 'w') as output_file:
    for ext, file_names in sorted(result.items()):
        output_file.write(f'.{ext}\n')
        for file_name in sorted(file_names):
            output_file.write(f'- - - {file_name}\n')

