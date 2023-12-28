import sys
n = int(input())

total_sum = 0
max_num = -sys.maxsize

for _ in range(n):
    num = int(input())
    total_sum += num
    if num > max_num:
        max_num = num

if total_sum == max_num * 2:
    print(f'Yes\nSum = {max_num}')
else:
    diff = abs(total_sum - max_num * 2)
    print(f'No\nDiff = {diff}')
