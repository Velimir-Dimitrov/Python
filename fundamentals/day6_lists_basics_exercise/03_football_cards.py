game_cards = input()
list_cards = game_cards.split(' ')
terminated = False
team_a = []
team_b = []
for player in range(1, 12):
    team_a.append(f"A-{player}")
    team_b.append(f"B-{player}")
for element in list_cards:
    if len(team_a) < 7 or len(team_b) < 7:
        terminated = True
        break
    if element in team_a:
        team_a.remove(element)
    elif element in team_b:
        team_b.remove(element)
print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if terminated:
    print("Game was terminated")
