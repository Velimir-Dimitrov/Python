number_of_commands = int(input())
registered_dict = {}

for command in range(number_of_commands):
    current_command = input().split(" ")
    if "register" in current_command:
        action, username, license_plate_number = current_command
        if username not in registered_dict:
            registered_dict[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    elif "unregister" in current_command:
        action, username = current_command
        if username not in registered_dict:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            registered_dict.pop(username)
[(print(f"{username} => {license_plate_number}")) for username, license_plate_number in registered_dict.items()]

