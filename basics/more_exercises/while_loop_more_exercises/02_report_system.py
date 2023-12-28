collect_goal = int(input())

cash_payment = 0
cash_completed = 0
card_payment = 0
card_completed = 0
type_payment = 0

while collect_goal > 0:
    command = input()
    if command == "End":
        print("Failed to collect required money for charity.")
        break
    cost = int(command)
    type_payment += 1
    if type_payment % 2 == 0:
        if cost <= 10:
            print("Error in transaction!")
        else:
            card_payment += cost
            collect_goal -= cost
            card_completed += 1
            print("Product sold!")
    else:
        if cost > 100:
            print("Error in transaction!")
        else:
            cash_payment += cost
            collect_goal -= cost
            cash_completed += 1
            print("Product sold!")
if collect_goal <= 0:
    print(f'Average CS: {cash_payment / cash_completed:.2f}')
    print(f'Average CC: {card_payment / card_completed:.2f}')