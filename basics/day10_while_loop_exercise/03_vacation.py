vacation_money = float(input())
current_savings = float(input())

days = 0
fail = 0
FAIL = False

while vacation_money > current_savings:
    action = input()
    funds = float(input())
    days += 1

    if action == "spend":
        current_savings -= funds
        if current_savings < 0:
            current_savings = 0
        fail += 1
    elif action == "save":
        current_savings += funds
        fail = 0

    if fail == 5:
        FAIL = True
        break

if FAIL:
    print(f"You can't save the money.\n{days}")

else:
    print(f"You saved the money for {days} days.")