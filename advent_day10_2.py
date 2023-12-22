f = open("input.txt", mode="r")


def next_pos_and_dir(grid, l, c, direction):
    if grid[l][c] == "F":
        if direction == "up":
            return l, c + 1, "right"
        if direction == "left":
            return l + 1, c, "down"
    if grid[l][c] == "-":
        if direction == "right":
            return l, c + 1, "right"
        if direction == "left":
            return l, c - 1, "left"
    if grid[l][c] == "|":
        if direction == "down":
            return l + 1, c, "down"
        if direction == "up":
            return l - 1, c, "up"
    if grid[l][c] == "L":
        if direction == "down":
            return l, c + 1, "right"
        if direction == "left":
            return l - 1, c, "up"
    if grid[l][c] == "J":
        if direction == "down":
            return l, c - 1, "left"
        if direction == "right":
            return l - 1, c, "up"
    if grid[l][c] == "7":
        if direction == "right":
            return l + 1, c, "down"
        if direction == "up":
            return l, c - 1, "left"

    return "no"


def find_start(grid):
    for l, line in enumerate(grid):
        for c, column in enumerate(line):
            if column == "S":
                return l, c


matrix = [[element for element in line.strip()] for line in f]

start_l, start_c = find_start(matrix)
start_dir = ""
if 0 <= start_l - 1 < len(matrix) and matrix[start_l - 1][start_c] in "F7|":
    start_dir = "up"
    start_l -= 1
elif  0 <= start_l + 1 < len(matrix) and matrix[start_l + 1][start_c] in "JL|":
    start_dir = "down"
    start_l += 1
elif  0 <= start_c + 1 < len(matrix[0]) and matrix[start_l][start_c + 1] in "-J7":
    start_dir = "right"
    start_c += 1
elif  0 <= start_c - 1 < len(matrix[0]) and matrix[start_l][start_c - 1] in "-FL":
    start_dir = "left"
    start_c -= 1


steps = 1
new_l, new_c, new_dir = next_pos_and_dir(matrix, start_l, start_c, start_dir)

while matrix[new_l][new_c] != "S":
    steps += 1
    old_l, old_c = new_l, new_c
    new_l, new_c, new_dir = next_pos_and_dir(matrix, new_l, new_c, new_dir)
    matrix[old_l][old_c] = "@"

for elem in matrix:
    print("".join(elem))
