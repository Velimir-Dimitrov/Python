from math import floor

tournaments = int(input())
current_points = int(input())

tournament_points = 0
win = 0

for _ in range(tournaments):
    position = input()
    if position == "W":
        win += 1
        tournament_points += 2000
    elif position == "F":
        tournament_points += 1200
    elif position == "SF":
        tournament_points += 720

percentage_win = win / tournaments * 100
avarage_points = tournament_points / tournaments

print(f"Final points: {current_points + tournament_points}\nAverage points: {floor(avarage_points)}\n{percentage_win:.2f}%")

