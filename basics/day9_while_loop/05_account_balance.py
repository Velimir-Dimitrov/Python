savings = 0

while True:
    command = input()
    if command == "NoMoreMoney":
        break
    deposit = float(command)
    if deposit >= 0:
        savings += deposit
        print(f"Increase: {deposit:.2f}")
    else:
        print("Invalid operation!")
        break
print(f"Total: {savings:.2f}")