change_money = float(input())
change_money = int(change_money * 100)
coin_counter = 0
while change_money > 0:
    if change_money >= 200:
        change_money -= 200
    elif change_money >= 100:
        change_money -= 100
    elif change_money >= 50:
        change_money -= 50
    elif change_money >= 20:
        change_money -= 20
    elif change_money >= 10:
        change_money -= 10
    elif change_money >= 5:
        change_money -= 5
    elif change_money >= 2:
        change_money -= 2
    elif change_money >= 1:
        change_money -= 1
    coin_counter += 1
print(coin_counter)
