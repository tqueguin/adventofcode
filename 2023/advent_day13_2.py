f = open("input.txt", mode="r")


def check_near_vertical_symetry(pattern, c1):
    cols_to_check = min(1 + c1, len(pattern[0]) - c1 - 1)
    defaults = 0
    for i in range(cols_to_check):
        for j in range(len(pattern)):
            if pattern[j][c1 - i] != pattern[j][c1 + 1 + i]:
                defaults += 1
    return defaults == 1


def check_near_horizontal_symetry(pattern, l1):
    rows_to_check = min(1 + l1, len(pattern) - l1 - 1)
    defaults = 0
    for i in range(rows_to_check):
        for j in range(len(pattern[0])):
            if pattern[l1 - i][j] != pattern[l1 + 1 + i][j]:
                defaults += 1
    return defaults == 1


patterns = [[list(i) for i in p.split("\n")] for p in f.read().split("\n\n")]

total = 0
for pattern_number, p in enumerate(patterns):
    for i in range(len(p[0]) - 1):
        if check_near_vertical_symetry(p, i):
            total += i + 1
    for i in range(len(p) - 1):
        if check_near_horizontal_symetry(p, i):
            total += 100 * (i + 1)

print(total)
