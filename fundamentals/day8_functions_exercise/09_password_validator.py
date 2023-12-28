def password_check(some_string):
    digit_counter = 0
    first_check_passed = False
    second_check_passed = False
    third_check_passed = False
    if 6 <= len(some_string) <= 10:
        first_check_passed = True
    for el in some_string:
        if el.isalpha():
            second_check_passed = True
        elif el.isnumeric():
            second_check_passed = True
            digit_counter += 1
        else:
            second_check_passed = False
            break
    if digit_counter >= 2:
        third_check_passed = True
    return first_check_passed, second_check_passed, third_check_passed


password_string = input()
criteria_one, criteria_two, criteria_three = password_check(password_string)
if not criteria_one:
    print("Password must be between 6 and 10 characters")
if not criteria_two:
    print("Password must consist only of letters and digits")
if not criteria_three:
    print("Password must have at least 2 digits")
if criteria_one and criteria_two and criteria_three:
    print("Password is valid")