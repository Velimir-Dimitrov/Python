turns = int(input())

total = 0

top9 = 0
top19 = 0
top29 = 0
top39 = 0
top50 = 0
invalid = 0

for _ in range(turns):
    number = int(input())
    if 0 <= number <= 9:
        total += number * 0.2
        top9 += 1
    elif 10 <= number <= 19:
        total += number * 0.3
        top19 += 1
    elif 20 <= number <= 29:
        total += number * 0.4
        top29 += 1
    elif 30 <= number <= 39:
        total += 50
        top39 += 1
    elif 40 <= number <=50:
        total += 100
        top50 += 1
    else:
        total /= 2
        invalid += 1

top9_percentage = top9 / turns * 100
top19_percentage = top19 / turns * 100
top29_percentage = top29 / turns * 100
top39_percentage = top39 / turns * 100
top50_percentage = top50 / turns * 100
invalid_percentage = invalid / turns * 100

print(f'{total:.2f}')
print(f"From 0 to 9: {top9_percentage:.2f}%")
print(f"From 10 to 19: {top19_percentage:.2f}%")
print(f"From 20 to 29: {top29_percentage:.2f}%")
print(f"From 30 to 39: {top39_percentage:.2f}%")
print(f"From 40 to 50: {top50_percentage:.2f}%")
print(f"Invalid numbers: {invalid_percentage:.2f}%")
