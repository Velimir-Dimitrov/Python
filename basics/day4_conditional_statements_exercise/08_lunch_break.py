from math import ceil

tv_series_name = input()
episode_length = int(input())
break_length = int(input())

lunch_length = break_length * 1/8
rest_length = break_length * 1/4

needed_time = episode_length + lunch_length + rest_length
diff = ceil(abs(break_length - needed_time))

if break_length >= needed_time:
    print(f'You have enough time to watch {tv_series_name} and left with {diff} minutes free time.')
else:
    print(f"You don't have enough time to watch {tv_series_name}, you need {diff} more minutes.")
