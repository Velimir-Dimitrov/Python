def drawing(num):
    if num == 0:
        return
    print("*" * num)
    drawing(num-1)
    print("#" * num)


num = int(input())
drawing(num)

## Inputs
# 2
# 5