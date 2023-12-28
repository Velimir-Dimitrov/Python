last_sector = input()
number_rolls = int(input())
number_odd_seats = int(input())

last_sector_digit = ord(last_sector)
total_seats = 0

for sector in range(65, last_sector_digit + 1):
    number_rolls += 1
    for roll in range(1, number_rolls):
        if roll % 2 != 0:
            for seat in range(97, 97 + number_odd_seats):
                print(f'{chr(sector)}{roll}{chr(seat)}')
                total_seats += 1
        else:
            for seat in range(97, 97 + number_odd_seats + 2):
                print(f'{chr(sector)}{roll}{chr(seat)}')
                total_seats += 1
print(total_seats)