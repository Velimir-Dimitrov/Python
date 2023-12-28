text = input()
encrypted_version = ""

for char in text:
    encrypted_version += chr((ord(char) + 3))
print(encrypted_version)