number_x1 = float(input())
number_y1 = float(input())
number_x2 = float(input())
number_y2 = float(input())
number_x = float(input())
number_y = float(input())

if (number_x1 <= number_x <= number_x2 and (number_y == number_y1 or number_y == number_y2)) or \
        (number_y1 <= number_y <= number_y2 and (number_x == number_x1 or number_x == number_x2)):
    print("Border")
else:
    print("Inside / Outside")
