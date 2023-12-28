destination = input()


while destination != "End":
    required_money = float(input())
    savings = 0
    while True:

        savings += float(input())
        if savings >= required_money:
           print(f"Going to {destination}!")
           break
    destination = input()




