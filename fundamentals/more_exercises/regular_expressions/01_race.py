def name_check(string):
    import re
    pattern = r"[A-Za-z]"
    letters = re.findall(pattern, string)
    return "".join(letters)


def distance_check(string):
    import re
    pattern = r"[0-9]"
    total = 0
    numbers = re.findall(pattern, string)
    for num in numbers:
        total += int(num)
    return total


participants = dict.fromkeys(input().split(", "), 0)

while True:
    command_line = input()
    if command_line == "end of race":
        break
    name = name_check(command_line)
    if name in participants:
        distance = distance_check(command_line)
        participants[name] += distance


sorted_ranking = sorted(participants.items(), key=lambda x:x[1], reverse=True)

print(f"1st place: {sorted_ranking[0][0]}\n2nd place: {sorted_ranking[1][0]}\n3rd place: {sorted_ranking[2][0]}")

