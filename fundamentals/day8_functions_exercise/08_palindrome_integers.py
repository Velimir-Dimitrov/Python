def palindrome_check(some_num):
    if some_num == some_num[::-1]:
        return True
    return False


string_with_numbers = input().split(", ")
for el in string_with_numbers:
    print(palindrome_check(el))