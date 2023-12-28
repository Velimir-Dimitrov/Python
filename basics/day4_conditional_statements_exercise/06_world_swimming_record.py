from math import floor

record_in_sec = float(input())
distance_in_metres = float(input())
time_per_meter = float(input())

total_time = distance_in_metres * time_per_meter
delay = floor(distance_in_metres // 15) * 12.5
personal = total_time + delay

if record_in_sec > personal:
    print(f'Yes, he succeeded! The new world record is {personal:.2f} seconds.')
else:
    print(f'No, he failed! He was {personal - record_in_sec:.2f} seconds slower.')

