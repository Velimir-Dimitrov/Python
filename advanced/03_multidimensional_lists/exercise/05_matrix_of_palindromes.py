rows, columns = [int(x) for x in input().split()]

char = ord('a')

for row in range(rows):
    for col in range(columns):
        print(f"{chr(char+row)}{chr(char+row+col)}{chr(char+row)}", end=' ')
    print()