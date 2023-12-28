def length_check(word):
    if 3 <= len(word) <= 16:
        return True


def contain_check(word):
    for char in word:
        if not char.isalnum() and not char == "_" and not char == "-":
            return False
    return True


def redundant_check(word):
    if " " in word:
        return False
    return True


def is_valid(word):
    if length_check(word) and redundant_check(word) and contain_check(word):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if is_valid(username):
        print(username)
