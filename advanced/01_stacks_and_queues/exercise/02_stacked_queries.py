number_lines = int(input())
stack = []

for line in range(number_lines):
    query = input().split()
    command = query[0]
    if command == "1":
        received_number = int(query[1])
        stack.append(received_number)
    elif len(stack) != 0:
        if command == "2":
            stack.pop()
        elif command == "3":
            print(max(stack))
        elif command == "4":
            print(min(stack))
while stack:
    print(stack.pop(), end="")
    if stack:
        print(", ", end="")
