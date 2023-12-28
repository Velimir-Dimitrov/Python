def travel(distance, fuel):
    if fuel >= distance:
        print(f"The spaceship travelled {distance} light-years.")
    else:
        print("Mission failed.")
        exit(0)
    return fuel - distance


def fight_or_flight(armour, ammunition, fuel):
    if ammunition >= armour:
        print(f"An enemy with {armour} armour is defeated.")
        return ammunition - armour, fuel
    else:
        if 2 * armour <= fuel:
            print(f"An enemy with {armour} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            exit(0)
    return ammunition, fuel - 2 * armour


def repair(added_value, ammunition, fuel):
    new_ammunition = ammunition + (added_value * 2)
    new_fuel = fuel + added_value
    print(f"Ammunitions added: {added_value * 2}.")
    print(f"Fuel added: {added_value}.")
    return new_ammunition, new_fuel


travel_route = input().split("||")
total_fuel = int(input())
total_ammunition = int(input())

for route in travel_route:
    if route == "Titan":
        print(f"You have reached Titan, all passengers are safe.")
        break
    command, value = route.split()
    if command == "Travel":
        total_fuel = travel(int(value), total_fuel)

    elif command == "Enemy":
        total_ammunition, total_fuel = fight_or_flight(int(value), total_ammunition, total_fuel)

    elif command == "Repair":
        total_ammunition, total_fuel = repair(int(value), total_ammunition, total_fuel)

