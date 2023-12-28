f = open("input.txt", mode="r")

# Parsing
l = f.readline()
seeds = [int(x) for x in l.split(":")[1].strip().split(" ")]
seeds2=[]
for i in range(len(seeds)//2):
    seeds2.append([seeds[2*i],seeds[2*i+1]])
seeds=seeds2

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


# Reverse search
i=20300000
notfound=True
while notfound:
    if i%100000==0:
        print(i/31000000*100,"%")
    seed=i
    for j in range(len(maps)-1,-1,-1):
        for tup in maps[j]:
            if seed>= tup[0] and seed<tup[0]+tup[2]:
                seed += tup[1]-tup[0]
                break

    for ranges in seeds:
        if seed >= ranges[0] and seed < ranges[0]+ranges[1]:
            print("Lowest is ",i)
            notfound=False
            break
        
    i+=1
