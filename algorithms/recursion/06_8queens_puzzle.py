SIZE = 8

def print_solution(queens):
    board = [['-' for _ in range(SIZE)] for _ in range(SIZE)]
    for row in range(SIZE):
        col = queens[row]
        board[row][col] = '*'
    for row in board:
        print(' '.join(row))
    print()


def place_queen(row, queens, cols, left_diagonals, right_diagonals):
    if row == SIZE:
        print_solution(queens)
        return

    for col in range(SIZE):
        if col in cols or (row - col) in left_diagonals or (row + col) in right_diagonals:
            continue


        queens[row] = col
        cols.add(col)
        left_diagonals.add(row - col)
        right_diagonals.add(row + col)


        place_queen(row + 1, queens, cols, left_diagonals, right_diagonals)


        queens[row] = -1
        cols.remove(col)
        left_diagonals.remove(row - col)
        right_diagonals.remove(row + col)

queens = [-1] * SIZE
place_queen(0, queens, set(), set(), set())

