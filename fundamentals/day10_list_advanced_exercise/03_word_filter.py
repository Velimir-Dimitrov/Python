words = input().split()
words_with_even_length = [word for word in words if len(word) % 2 == 0]
print("\n".join(words_with_even_length))