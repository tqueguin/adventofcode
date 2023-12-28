f = open("input.txt", mode="r")

# Parsing
l = f.readline()
seeds = [int(x) for x in l.split(":")[1].strip().split(" ")]

maps=[]
for line in f:
    if line == "\n":
        maps.append([])
    else:
        if "map" in line:
            continue
        else:
            a=int(line.split(" ")[0])
            b=int(line.split(" ")[1])
            c=int(line.split(" ")[2])
            maps[-1].append((a,b,c))

mini=-1

for seed in seeds:
    for j in range(len(maps)):
        for tup in maps[j]:
            if seed>= tup[1] and seed<tup[1]+tup[2]:
                seed += tup[0]-tup[1]
                break
    if mini==-1 or seed<mini:
        mini=seed

print(mini)
    
