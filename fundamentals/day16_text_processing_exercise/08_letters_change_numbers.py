sequence_of_strings = input().split()
total_sum = 0
for current_string in sequence_of_strings:
    first_letter = current_string[0]
    last_letter = current_string[-1]
    number = int(current_string[1:len(current_string)-1])
    current_string_sum = 0
    if first_letter.isupper():
        current_string_sum = number / (ord(first_letter) - 64)
    elif first_letter.islower():
        current_string_sum = number * (ord(first_letter) - 96)
    if last_letter.isupper():
        current_string_sum -= (ord(last_letter) - 64)
    elif last_letter.islower():
        current_string_sum += (ord(last_letter) - 96)
    total_sum += current_string_sum

print(f'{total_sum:.2f}')


# sequence_of_strings = input()
# total_sum = 0
# current_string_sum = 0
# letter_number = 0
# number_string = ""
# divide = False
# multiple = False
#
# for index in range(len(sequence_of_strings)):
#     if sequence_of_strings[index] == " ":
#         total_sum += float(current_string_sum)
#         number_string = ""
#         current_string_sum = 0
#     elif (divide or multiple) and sequence_of_strings[index].isalpha():
#         if divide:
#             current_string_sum = float(number_string) / letter_number
#             divide = False
#         if multiple:
#             current_string_sum = float(number_string) * letter_number
#             multiple = False
#         if sequence_of_strings[index].isupper():
#             letter_number = ord(sequence_of_strings[index]) - 64
#             current_string_sum -= letter_number
#         if sequence_of_strings[index].islower():
#             letter_number = ord(sequence_of_strings[index]) - 96
#             current_string_sum += letter_number
#     elif sequence_of_strings[index].isalpha() and sequence_of_strings[index + 1].isnumeric():
#         if sequence_of_strings[index].isupper():
#             letter_number = ord(sequence_of_strings[index]) - 64
#             divide = True
#         else:
#             letter_number = ord(sequence_of_strings[index]) - 96
#             multiple = True
#     elif sequence_of_strings[index].isnumeric():
#         number_string += sequence_of_strings[index]
# print(f'{total_sum + current_string_sum:.2f}')