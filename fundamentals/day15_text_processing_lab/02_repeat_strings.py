sequence_of_strings = input().split()
single_string = ""

for string in sequence_of_strings:
    single_string += string * len(string)
print(single_string)
