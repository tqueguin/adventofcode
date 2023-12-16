f = open("input.txt", mode="r")

def vert_sym(g):
    return


patterns = []
grid = []
for i, line in enumerate(f):
    if line == "\n":
        patterns.append(grid)
        grid = []
    else:
        grid.append([elem for elem in line.strip()])

for pattern in patterns:
    vert_sym(pattern)
