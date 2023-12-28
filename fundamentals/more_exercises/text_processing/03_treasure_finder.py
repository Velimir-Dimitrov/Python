def find_type_treasure(string_message):
    slice_index = string_message.index("&")
    new_string = string_message[slice_index+1::]
    new_slice_index = new_string.index("&")
    treasure_type = new_string[0:new_slice_index]
    return treasure_type


def find_coordinates(string_message):
    start_index = string_message.index("<")
    end_index = string_message.index(">")
    coordinates = string_message[start_index+1:end_index]
    return coordinates


key_sequence = input().split(" ")

while True:
    some_string = input()
    if some_string == "find":
        break
    decrypted_message = ""
    for index in range(len(some_string)):
        string_char = some_string[index]
        if index == len(key_sequence):
            key_sequence += key_sequence
        new_string_char = ord(string_char) - int(key_sequence[index])
        decrypted_message += chr(new_string_char)
    type_of_treasure = find_type_treasure(decrypted_message)
    treasure_coordinates = find_coordinates(decrypted_message)
    print(f"Found {type_of_treasure} at {treasure_coordinates}")


# secret_key = [int(x) for x in input().split()]
# secret_msg = input()
# how_long = len(secret_key)
# while secret_msg != "find":
#     secret_text = "".join([chr(ord(secret_msg[i]) - secret_key[i % how_long]) for i in range(len(secret_msg))])
#     item = secret_text.split("&")[-2]
#     location = secret_text.split("<")[-1][:-1]
#     print(f"Found {item} at {location}")
#     secret_msg = input()