detergent = int(input())
total_litres_detergent = detergent * 750

pots_counter = 0
dishes = 0
pots = 0

while total_litres_detergent >= 0 :
    command = input()
    if command == "End":
        break
    number_cookware = int(command)
    pots_counter += 1

    if pots_counter % 3 == 0:
        pots += number_cookware
        total_litres_detergent -= number_cookware * 15
    else:
        dishes += number_cookware
        total_litres_detergent -= number_cookware * 5
if total_litres_detergent >= 0:
    print(f"Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {total_litres_detergent} ml.")
else:
    print(f"Not enough detergent, {(abs(total_litres_detergent))} ml. more necessary!")
