screening_type = input()
rolls = int(input())
columns = int(input())
price = 0
seats = rolls * columns

if screening_type == "Premiere":
    price = 12.00
elif screening_type == "Normal":
    price = 7.50
elif screening_type == "Discount":
    price = 5.00
earnings = seats * price
print(f'{earnings:.2f} leva')