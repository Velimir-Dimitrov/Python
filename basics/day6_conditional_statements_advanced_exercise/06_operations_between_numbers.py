n1 = int(input())
n2 = int(input())
operator = input()
result = 0
DATA_ERROR = False

if operator == "-":
    result = n1 - n2
elif operator == "+":
    result = n1 + n2
elif operator == "*":
    result = n1 * n2
elif operator == "/":
    if n2 != 0:
        result = n1 / n2
    else:
        DATA_ERROR = True
elif operator == "%":
    if n2 != 0:
        result = n1 % n2
    else:
        DATA_ERROR = True

if DATA_ERROR:
    print(f"Cannot divide {n1} by zero")
elif operator == "-" or operator == "+" or operator == "*":
    if result % 2 == 0:
        print(f'{n1} {operator} {n2} = {result} - even')
    else:
        print(f'{n1} {operator} {n2} = {result} - odd')
elif operator == "/":
    print(f'{n1} {operator} {n2} = {result:.2f}')
elif operator == "%":
    print(f'{n1} {operator} {n2} = {result}')
