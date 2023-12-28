n = int(input())

for dupe in range(n):
    string = input()
    for char in string:
        if ord(char) == 95 or ord(char) == 44 or ord(char) == 46:
            print(f"{string} is not pure!")
            break
    else:
        print(f"{string} is pure.")