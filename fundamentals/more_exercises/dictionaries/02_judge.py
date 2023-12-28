def save_info(name, event, score, event_dictionary):
    if event in event_dictionary:
        if name in event_dictionary[event] and event_dictionary[event][name] >= score:
            return event_dictionary
        event_dictionary[event][name] = score
        return event_dictionary
    event_dictionary[event] = {name: score}
    return event_dictionary


contests_dict = {}
while True:
    command = input()
    if command == "no more time":
        break
    username, contest, points = [int(x) if x.isdigit() else x for x in command.split(" -> ")]
    contests_dict = save_info(username, contest, points, contests_dict)

standing_dict = {}

for contest in contests_dict:
    number_participants = len(contests_dict[contest])
    print(f"{contest}: {number_participants} participants")
    sorted_participants = dict(sorted(contests_dict[contest].items(), key=lambda x:x[1], reverse=True))
    for index, participant in enumerate(sorted_participants):
        position = index + 1
        points = sorted_participants[participant]
        if participant not in standing_dict:
            standing_dict[participant] = 0
        standing_dict[participant] += points
        print(f"{position}. {participant} <::> {points}")
print("Individual standings:")
sorted_standing_dict = dict(sorted(standing_dict.items(), key=lambda x:x[1], reverse=True))
for index, name in enumerate(sorted_standing_dict):
    standing = index + 1
    total_points = sorted_standing_dict[name]
    print(f"{standing}. {name} -> {total_points}")


