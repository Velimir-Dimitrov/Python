number_of_pairs = int(input())

current_sum = 0
previous_sum = 0
current_diff = 0
max_diff = 0

for i in range(2 * number_of_pairs):
    number = int(input())
    if i % 2 == 0:
        current_sum = number
    else:
        current_sum += number
        if i == 1:
            previous_sum = current_sum
        else:
            current_diff = abs(previous_sum - current_sum)
            previous_sum = current_sum
            if max_diff < current_diff:
                max_diff = current_diff
if max_diff == 0:
    print(f'Yes, value={previous_sum}')
else:
    print(f"No, maxdiff={max_diff}")

#alterinative
#pairs = int(input())
#previous_sum = int(input()) + int(input())
#max_diff = 0
#for i in range(pairs - 1):
    #current_sum = int(input()) + int(input())
    #if abs(previous_sum - current_sum) > max_diff:
        #max_diff = abs(previous_sum - current_sum)
    #previous_sum = current_sum
#if max_diff == 0:
    #print(f'Yes, value={previous_sum}')
#else:
    #print(f"No, maxdiff={max_diff}")