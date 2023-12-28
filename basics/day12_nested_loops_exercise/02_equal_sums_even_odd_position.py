number1 = int(input())
number2 = int(input())



for x in range(number1, number2 + 1):
    x = str(x)
    while int(x[0]) + int(x[2]) + int(x[4]) == int(x[1]) + int(x[3]) + int(x[5]):
        print(x, end = " " )
        break
    else:
        continue



    #even_sum = 0
    #odd_sum = 0

    #for index, digit in enumerate(x):
        #if index % 2 == 0:
            #even_sum += int(digit)
        #else:
            #odd_sum += int(digit)
    #if even_sum == odd_sum:
        #print(x, end= " ")