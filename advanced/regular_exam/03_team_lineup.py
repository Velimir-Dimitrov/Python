def team_lineup(*players_list):
    players_dictionary = {}
    for player_and_country in players_list:
        current_player, country = player_and_country
        if country not in players_dictionary:
            players_dictionary[country] = []
        players_dictionary[country].append(current_player)
    result = ''
    for country, players in sorted(players_dictionary.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]) ):
        result += f"{country}:\n"
        for player in players:
            result += f"  -{player}\n"
    return result


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))
print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))
print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))


