days_off = int(input())

working_days = 365 - days_off
play_time = working_days * 63 + days_off * 127

diff = abs(play_time - 30000)
hours = diff // 60
minutes = diff % 60

if play_time >= 30000:
    print("Tom will run away")
    print(f'{hours} hours and {minutes} minutes more for play')
elif play_time < 30000:
    print("Tom sleeps well")
    print(f'{hours} hours and {minutes} minutes less for play')

