text = input()
result = 0

for i in text:
    if i == "a":
        result += 1
    if i == "e":
        result += 2
    if i == "i":
        result += 3
    if i == 'o':
        result += 4
    if i == "u":
        result += 5

print(result)