message = input().split(" ")
deciphered_message = []

for el in message:
    current_message = []
    first_letter_digit = ""
    for index in range(0, len(el)):
        if el[index].isnumeric():
            first_letter_digit += el[index]
        else:
            current_message.append(el[index])
    first_letter = chr(int(first_letter_digit))
    current_message.insert(0, first_letter)
    current_message[1],current_message[-1] = current_message[-1], current_message[1]

    deciphered_message.append(''.join(current_message))
print(*deciphered_message)


