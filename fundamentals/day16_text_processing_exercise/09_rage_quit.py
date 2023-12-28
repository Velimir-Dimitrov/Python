message = input().upper()
rage_message = ""
current_string = ""
current_multiplier = ""

for element in message:
    if element.isnumeric():
        current_multiplier += element
    elif current_multiplier and not element.isnumeric():
        rage_message += current_string * int(current_multiplier)
        current_multiplier = ""
        current_string = element
    else:
        current_string += element

rage_message += current_string * int(current_multiplier)
print(f"Unique symbols used: {len(set(rage_message))}")
print(rage_message)