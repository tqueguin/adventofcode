f = open("input.txt", "r")

grid = []
for line in f:
    grid.append([i if i != "S" else True for i in line.strip()])
grids=[grid]

for step in range(64):
    grids.append([])
    for i in range(len(grid)):
        grids[step+1].append([])
        for j in range(len(grid[i])):
            grids[step+1][i].append(grids[step][i][j])

    old_grid = grids[step]
    new_grid = grids[step+1]
    for i in range(len(old_grid)):
        for j in range(len(old_grid[i])):
            if new_grid[i][j] != "#":
                new_grid[i][j] = 0
                top = old_grid[i-1][j] if i - 1 >= 0 else old_grid


                if i - 1 >= 0 and type(old_grid[i - 1][j]) is bool and old_grid[i - 1][j] is True:
                    new_grid[i][j] = True
                elif i + 1 < len(grid) and type(old_grid[i + 1][j]) is bool and old_grid[i+1][j] is True:
                    new_grid[i][j] = True
                elif j - 1 >= 0 and type(old_grid[i][j - 1]) is bool and old_grid[i][j-1] is True:
                    new_grid[i][j] = True
                elif j + 1 < len(grid[i]) and type(old_grid[i][j + 1]) is bool and old_grid[i][j+1] is True:
                    new_grid[i][j] = True



total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if new_grid[i][j] != "#" and new_grid[i][j] is True:
            total += 1
print(total)
