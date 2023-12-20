f = open("input.txt", mode="r")

total = 0
for line in f:
    total_line = 0
    springs = line.split(" ")[0]*5
    expected_groups = [int(i) for i in line.split(" ")[1].split(",")]*5

    groups = [e for e in springs.split(".") if e != ""]









print(total)
