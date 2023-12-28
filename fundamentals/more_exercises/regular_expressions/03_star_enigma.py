import re


def decrypt(key, string):
    message = ""
    for index in range(len(string)):
        new_char = ord(string[index]) - key
        message += chr(new_char)
    return message


number_of_lines = int(input())
key_chars = r"(?i)s|t|a|r"
pattern = r"[^\@\-\!\:\>]*@([A-Z][a-z]+)[^\@\-\!\:\>]*:(\d+)[^\@\-\!\:\>]*!([A|D])![^\@\-\!\:\>]*->(\d+)"
attacked_planets = []
destroyed_planets = []

for line in range(number_of_lines):
    current_line = input()
    chars = re.findall(key_chars, current_line)
    key_count = len(chars)
    decrypted_message = decrypt(key_count, current_line)
    final_message = re.findall(pattern, decrypted_message)
    if final_message:
        planet_name, planet_population, attack_type, soldier_count = final_message[0]
        if attack_type == "A":
            attacked_planets.append(planet_name)
        elif attack_type == "D":
            destroyed_planets.append(planet_name)
print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets):
    print(f'-> {planet}')
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in sorted(destroyed_planets):
    print(f'-> {planet}')
