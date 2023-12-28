line_1 = input().split(" ")
line_2 = input().split(" ")
line_3 = input().split(" ")
winner_player_1 = False
winner_player_2 = False

for a in range(len(line_1)):
    for b in range(len(line_2)):
        for c in range(len(line_3)):
            if line_1[0] == line_1[1] == line_1[2] != "0" or \
                    line_1[0] == line_2[1] == line_3[2] != "0" or \
                    line_1[0] == line_2[0] == line_3[0] != "0":
                if line_1[0] == "1":
                    winner_player_1 = True
                    break
                else:
                    winner_player_2 = True
                    break
            elif line_2[0] == line_2[1] == line_2[2] != "0" or \
                    line_1[1] == line_2[1] == line_3[1] != "0" or \
                    line_1[2] == line_2[1] == line_3[0] != "0":
                if line_2[1] == "1":
                    winner_player_1 = True
                    break
                else:
                    winner_player_2 = True
                    break
            elif line_3[2] == line_3[1] == line_3[0] != "0" or \
                    line_3[2] == line_2[2] == line_1[2] != "0":
                if line_3[2] == "1":
                    winner_player_1 = True
                    break
                else:
                    winner_player_2 = True
                    break

if winner_player_1:
    print("First player won")
elif winner_player_2:
    print("Second player won")
else:
    print("Draw!")

