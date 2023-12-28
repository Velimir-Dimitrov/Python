pages = int(input())
pages_per_hour = int(input())
amount_of_days = int(input())
hours_per_day = pages // pages_per_hour // amount_of_days
print(hours_per_day)