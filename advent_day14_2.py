f = open("input.txt", mode="r")

grid = []
for line in f:
    grid.append([elem for elem in line.strip()])

def tilt_grid_north(g):
    for j in range(len(g)):
        max_weight = len(grid)
        weight_col = 0
        total_weight_col = 0
        for i in range(len(grid[j])):
            if grid[i][j] == '#':
                total_weight_col += int((2 * max_weight - weight_col + 1) / 2 * weight_col)
                max_weight = len(grid) - i - 1
                weight_col = 0
                continue
            if grid[i][j] == 'O':
                weight_col += 1

        total_weight_col += int((2 * max_weight - weight_col + 1) / 2 * weight_col)

        print(total_weight_col)
        total_weight += total_weight_col


for i in range(1000000000):
