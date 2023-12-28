words = [el for el in input().split() if el == el[::-1]]
palindrome_check = words.count(input())
print(words)
print(f'Found palindrome {palindrome_check} times')