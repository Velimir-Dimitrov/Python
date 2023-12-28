n = int(input())
for x in range(1111, 9999 + 1):
    y = str(x)
    is_special = True
    for char in y:
        if char == "0" or n % int(char) != 0:
            is_special = False
            break
    if is_special:
        print(y, end = ' ')


#n = int(input())
#for i in range(1, 10):
    #if n % i != 0:
        #continue
    #for y in range(1, 10):
        #if y == 0 or n % y != 0:
            #continue
        #for x in range(1, 10):
            #if x == 0 or n % x != 0:
                #continue
            #for z in range(1, 10):
                #if z == 0 or n % z != 0:
                    #continue
                #else:
                    #print(f'{i}{y}{x}{z}', end =' ')