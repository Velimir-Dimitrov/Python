n = int(input())
total_sum = 0
if 0 > n or n > 20:
    exit()

for _ in range(n):
    letter = input()
    total_sum += ord(letter)
print(f"The sum equals: {total_sum}")

# print(f"The sum equals: {sum(ord(input()) for _ in range(int(input())))}")