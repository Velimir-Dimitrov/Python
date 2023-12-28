n = int(input())
matrix = [[x for x in list(input())] for row in range(n)]
knights = [[row, col] for row in range(n) for col in range(n) if matrix[row][col] == "K"]

knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

removed_knights = 0

while True:
    knight_with_most_attacks = []
    most_knight_attacks = 0
    for current_knight in knights:
        knight_attacks = 0
        for move in knight_moves:
            row = current_knight[0] + move[0]
            col = current_knight[1] + move[1]
            if (0 <= row < n and 0 <= col < n) and matrix[row][col] == "K":
                knight_attacks += 1
        if knight_attacks > most_knight_attacks:
            most_knight_attacks = knight_attacks
            knight_with_most_attacks = current_knight
    if most_knight_attacks == 0:
        break
    knights.remove(knight_with_most_attacks)
    removed_knights += 1
    r, l = knight_with_most_attacks
    matrix[r][l] = '0'
print(removed_knights)