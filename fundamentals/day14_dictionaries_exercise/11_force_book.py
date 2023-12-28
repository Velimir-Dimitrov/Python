def add(side, user):
    for value in force_dict.values():
        if user in value:
            return
    if side not in force_dict.keys():
        force_dict[side] = []
    force_dict[side].append(user)


def switch(user, side):
    for key, values in force_dict.items():
        if user in values:
            force_dict[key].remove(user)
            break
    if side not in force_dict.keys():
        force_dict[side] = []
    force_dict[side].append(user)
    print(f"{user} joins the {side} side!")


force_dict = {}
while True:
    command = input()
    if command == "Lumpawaroo":
        break
    elif "|" in command:
        force_side, force_user = command.split(" | ")
        add(force_side, force_user)
    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        switch(force_user, force_side)

for side, members in force_dict.items():
    if members:
        print(f"Side: {side}, Members: {len(members)}")
        for member in members:
            print(f"! {member}")

# 80/100??
# force_dict = {}
# while True:
#     command = input()
#     if command == "Lumpawaroo":
#         break
#     elif "|" in command:
#         force_side, force_user = command.split(" | ")
#         if force_side not in force_dict.keys() and force_user not in force_dict.values():
#             force_dict[force_side] = []
#         elif [True for value in force_dict.values() if force_user in value]:
#             continue
#         force_dict[force_side].append(force_user)
#     elif "->" in command:
#         force_user, force_side  = command.split(" -> ")
#         if [True for value in force_dict.values() if force_user in value]:
#             for force, users in force_dict.items():
#                 if force_user in users:
#                     force_dict[force].remove(force_user)
#                     break
#         elif force_side not in force_dict.keys() and force_user not in force_dict.values():
#             force_dict[force_side] = []
#         force_dict[force_side].append(force_user)
#         print(f"{force_user} joins the {force_side} side!")
#
# for side, members in force_dict.items():
#     if members:
#         print(f"Side: {side}, Members: {len(members)}")
#         for member in members:
#             print(f"! {member}")