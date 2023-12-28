from string import punctuation

with open('line_numbers.txt', "w+") as file_input:
    while True:
        text_line = input()
        if text_line == '':
            break
        file_input.write(text_line + '\n')
    file_input.seek(0)

    with open('result_line_numbers.txt', 'w+') as file_result:
        for line_num, line_content in enumerate(file_input.readlines(), start=1):
            punctuation_count = 0
            letters = 0
            for el in line_content:
                if el in punctuation:
                    punctuation_count += 1
                elif el.isalpha():
                    letters += 1
            file_result.write(f'Line {line_num}: ' + line_content.strip() + f' ({letters})({punctuation_count})\n')
        file_result.seek(0)
        print(file_result.read())



