def calculate(command, first_num, second_num):
    result = None
    if command == "multiply":
        result = first_num * second_num
    elif command == "divide":
        result = first_num // second_num
    elif command == "add":
        result = first_num + second_num
    elif command == "subtract":
        result = first_num - second_num
    return result


string_operator = input()
a = int(input())
b = int(input())
# res = calculate(string_operator, a, b)
# print(res)
print(calculate(string_operator, a, b))