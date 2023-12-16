import math

f = open("input.txt", mode="r")

dirs = f.readline().strip()
f.readline()

d = {}

for line in f.readlines():
    line = line.strip()
    curr = line.split("=")[0].strip()
    left = line.split("=")[1].strip().split(",")[0][1:]
    right = line.split("=")[1].strip().split(",")[1].strip()[:-1]
    d[curr]=(left,right)

steps = 0
currents = [elem for elem in d if elem[2] == "A"]
goals = [elem for elem in d if elem[2] == "Z"]
cycle_size = [0] * len(currents)

while cycle_size.count(0) > 0:
    for i, current in enumerate(currents):
        if currents[i] in goals:
            cycle_size[i] = steps

        if dirs[steps % len(dirs)] == "L":
            currents[i] = d[current][0]
        else:
            currents[i] = d[current][1]

    steps += 1


print(math.lcm(*cycle_size))
