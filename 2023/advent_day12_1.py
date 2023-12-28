import timeit

start = timeit.default_timer()

f = open("input.txt", mode="r")

total = 0
nl = 0
for line in f:
    springs = line.split(" ")[0]
    groups = [int(i) for i in line.split(" ")[1].split(",")]
    sum_groups = sum(groups)
    total_line = 0
    count=springs.count("?")
    count_deja=springs.count("#")

    for i in range(2 ** count):
        arr = format(i, "b").zfill(count)
        if count_deja + arr.count("1") < sum_groups:
            continue

        s = [sp for sp in springs]
        for j in range(count):
            if arr[j] == "0":
                s[s.index("?")] = "#"
            else:
                s[s.index("?")] = "."

        lis = [i.strip() for i in "".join(s).replace(".", " ").split(" ") if i != ""]

        valid = True
        if len(groups) != len(lis):
            valid = False
        if valid:
            for j, group in enumerate(groups):
                if len(lis[j]) != group:
                    valid = False
        if valid:
            total_line += 1

    total += total_line
    nl+=1
    print(nl)
print(total)
print(timeit.default_timer()-start)