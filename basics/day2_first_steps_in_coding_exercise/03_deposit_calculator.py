deposit = float(input())
months = int(input())
year_percentage = float(input()) / 100

earnings = deposit + months * (( deposit * year_percentage) / 12)
print(earnings)