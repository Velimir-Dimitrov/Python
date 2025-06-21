class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size

def find_area(row, col, matrix):
    if 0 > row or row >= len(matrix) or 0 > col or col >= len(matrix[0]):
        return 0
    if matrix[row][col] != '-':
        return 0

    matrix[row][col] = 'v'
    size = 1
    size += find_area(row + 1, col, matrix) #down
    size += find_area(row, col + 1, matrix) #right
    size += find_area(row - 1, col, matrix) #up
    size += find_area(row, col - 1, matrix) #left
    return size


rows = int(input())
columns = int(input())
matrix = [list(input()) for row in range(rows)]
found_areas = []

for row in range(rows):
    for col in range(columns):
        size = find_area(row, col, matrix)
        if size == 0:
            continue
        found_areas.append(Area(row, col, size))

print(f"Total areas found: {len(found_areas)}")
for position, area in enumerate(sorted(found_areas, key=lambda a: (-a.size, a.row, a.col)), 1):
    print(f"Area #{position} at ({area.row}, {area.col}), size: {area.size}")


# # Inputs
# 4
# 9
# ---*---*-
# ---*---*-
# ---*---*-
# ----*-*--
#
# 5
# 10
# *--*---*--
# *--*---*--
# *--*****--
# *--*---*--
# *--*---*--
#
