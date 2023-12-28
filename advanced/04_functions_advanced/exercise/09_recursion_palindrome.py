def palindrome(some_word, some_index):
    if some_index == len(some_word) // 2:
        return f"{some_word} is a palindrome"
    elif some_word[some_index] == some_word[-1 - some_index]:
        return palindrome(some_word, some_index + 1)
    else:
        return f"{some_word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peep", 0))
print(palindrome("pestaep", 0))