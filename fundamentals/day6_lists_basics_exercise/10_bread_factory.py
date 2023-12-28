work_day_events = input().split('|')
current_energy = 100
current_coins = 100
failed_event = False
for event in work_day_events:
    if "rest-" in event:
        energy = event.replace("rest-", '')
        if current_energy + int(energy) > 100:
            print(f"You gained {abs(100 - current_energy)} energy.")
            current_energy = 100
        else:
            current_energy += int(energy)
            print(f"You gained {energy} energy.")
        print(f"Current energy: {current_energy}.")
    elif "order-" in event:
        coin = event.replace("order-", '')
        if current_energy - 30 >= 0:
            current_energy -= 30
            current_coins += int(coin)
            print(f"You earned {coin} coins.")
        else:
            current_energy += 50
            print("You had to rest!")
    else:
        ingredient = event.split("-")
        if current_coins >= int(ingredient[1]):
            current_coins -= int(ingredient[1])
            print(f"You bought {ingredient[0]}.")
        else:
            print(f"Closed! Cannot afford {ingredient[0]}.")
            failed_event = True
            break
if not failed_event:
    print(f'Day completed!\nCoins: {current_coins}\nEnergy: {current_energy}')

