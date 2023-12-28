f = open("input.txt", "r")

grid = []
for line in f:
    l = []
    for elem in line.strip():
        l.append(elem)
    if '#' not in line:
        grid.append(l.copy())
    grid.append(l)


no_gal_cols = []
for i in range(len(grid[0])):
    no_gal_in_col = True
    for j in range(len(grid)):
        if grid[j][i] == '#':
            no_gal_in_col = False
    if no_gal_in_col:
        no_gal_cols.append(i)

inserts = 0
print(no_gal_cols)
for col_index in no_gal_cols:
    for j in range(len(grid)):
        grid[j].insert(col_index+inserts, ".")
    inserts+=1

galaxies = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "#":
            galaxies.append((i,j))

distance = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        distance += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

for t in grid:
    print(" ".join(t))
print(distance)
