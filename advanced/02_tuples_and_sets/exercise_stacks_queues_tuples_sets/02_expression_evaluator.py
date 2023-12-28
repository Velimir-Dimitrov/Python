string_expression = tuple(input().split())
number_list = []

for el in string_expression:
    if el == "-":
        number_list = [number_list[0]-sum(number_list[1:])]
    elif el == "+":
        number_list = [sum(number_list)]
    elif el == "*":
        for x in number_list[1:]:
            number_list = [number_list[0] * x]
    elif el == "/":
        for x in number_list[1:]:
            number_list = [number_list[0] // x]
    else:
        number_list.append(int(el))
print(*number_list)