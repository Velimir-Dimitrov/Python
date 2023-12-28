import re

text = input().lower()
word = input()
pattern = fr"\b{word}\b"
# pattern = fr"(?i)\b{word}\b"
findings = re.findall(pattern, text)  # re.IGNORECASE
print(len(findings))