key = int(input())
number_of_lines = int(input())
decrypted_message = ''

for _ in range(number_of_lines):
    case = input()
    decrypted_message += chr(ord(case) + key)
print(decrypted_message)