while True:
    final_result = ''
    command = input()
    if command == "End":
        break
    elif command == "SoftUni":
        continue
    for char in command:
        final_result += char * 2
    print(final_result)

