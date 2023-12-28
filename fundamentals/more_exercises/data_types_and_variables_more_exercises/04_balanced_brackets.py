n = int(input())
opened_brackets = False
invalid = False

for _ in range(n):
    command = input()
    if len(command) > 1:
        continue
    if ord(command) == 40 and not opened_brackets:
        opened_brackets = True
    elif opened_brackets and ord(command) == 41:
        opened_brackets = False
    elif ord(command) == 40:
        invalid = True
    elif ord(command) == 41:
        invalid = True
if invalid or opened_brackets:
    print("UNBALANCED")
else:
    print("BALANCED")