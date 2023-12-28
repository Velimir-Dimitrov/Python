from collections import deque
parentheses_text = deque([el for el in input()])
start_parentheses = "[{("
end_parentheses = "]})"
counter = len(parentheses_text)

while parentheses_text and counter != 0:

    if parentheses_text[0] in start_parentheses:
        index = start_parentheses.index(parentheses_text[0])
        if parentheses_text[1] == end_parentheses[index]:
            parentheses_text.popleft()
            parentheses_text.popleft()
            counter = len(parentheses_text)
            continue
    parentheses_text.rotate(-1)
    counter -= 1

if parentheses_text:
    print("NO")
else:
    print("YES")