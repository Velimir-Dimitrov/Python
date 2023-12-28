punctuation = ["-", ",", ".", "!", "?"]

with open('01_text.txt', "w+") as f:
    while True:
        text_line = input()
        if text_line == '':
            break
        f.write(text_line + '\n')
    f.seek(0)

    for num_line, content_line in enumerate(f.readlines(), start=1):
        if num_line % 2:
            current_line = content_line
            for el in current_line:
                if el in punctuation:
                    current_line = current_line.replace(el, '@')
            print(" ".join(reversed(current_line.split())))






