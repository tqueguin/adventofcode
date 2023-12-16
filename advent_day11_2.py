import timeit

f = open("input.txt", "r")


def no_gal_in_column(g, c):
    cond = True
    for i in range(len(g)):
        if g[i][c] == "#":
            cond = False
    return cond


def no_gal_in_line(g, l):
    return "#" not in g[l]


start = timeit.default_timer()

grid = []
for line in f:
    l = []
    for elem in line.strip():
        l.append(elem)
    grid.append(l)

galaxies = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "#":
            galaxies.append((i, j))

distance = 0
empty_cols = set()
empty_rows = set()
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        g1_x = galaxies[i][0]
        g2_x = galaxies[j][0]
        g1_y = galaxies[i][1]
        g2_y = galaxies[j][1]
        minx = min(g1_x, g2_x)
        maxx = max(g1_x, g2_x)
        miny = min(g1_y, g2_y)
        maxy = max(g1_y, g2_y)

        factor = 1000000
        distance_pair = 0
        for k in range(minx + 1, maxx + 1):
            if k not in empty_rows:
                if no_gal_in_line(grid, k):
                    empty_rows.add(k)
                    distance_pair += factor

            else:
                distance_pair += 1

        for l in range(miny + 1, maxy + 1):
            if no_gal_in_column(grid, l):
                distance_pair += factor
            else:
                distance_pair += 1

        distance += distance_pair
print(distance)
print(timeit.default_timer()-start)