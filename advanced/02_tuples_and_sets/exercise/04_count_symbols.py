text = tuple(input())
unique_symbols = {}

for element in text:
    if element not in unique_symbols:
        unique_symbols[element] = text.count(element)
sorted_symbols = sorted(unique_symbols)

for symbol in sorted_symbols:
    print(f"{symbol}: {unique_symbols[symbol]} time/s")