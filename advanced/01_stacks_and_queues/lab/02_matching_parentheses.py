random_string = input()
parentheses = []

for index in range(len(random_string)):
    if random_string[index] == "(":
        parentheses.append(index)
    elif random_string[index] == ")":
        start_parentheses = parentheses.pop()
        end_parentheses = index + 1
        print(random_string[start_parentheses:end_parentheses])