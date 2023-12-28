import re
text = input()
words = []
pattern = r"\b_([a-zA-Z]*)\b"
result = re.findall(pattern, text)
print(*result, sep=",")