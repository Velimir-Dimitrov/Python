n = int(input())
odd_sum = 0
even_sum = 0

for position in range(1, n + 1):
    num = int(input())
    if position % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

if even_sum == odd_sum:
    print(f"Yes\nSum = {even_sum}")
else:
    diff = abs(even_sum - odd_sum)
    print(f"No\nDiff = {diff}")

