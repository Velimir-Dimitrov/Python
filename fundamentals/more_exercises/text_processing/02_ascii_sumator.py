start_char = input()
end_char = input()
random_string = input()

start_num = ord(start_char)
end_num = ord(end_char)

ascii_sum = 0

for el in random_string:
    if start_num < ord(el) < end_num:
        ascii_sum += ord(el)
print(ascii_sum)