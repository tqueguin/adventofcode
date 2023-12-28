f = open("input.txt", mode="r")

dirs=f.readline().strip()
f.readline()

d={}

for line in f.readlines():
    line = line.strip()
    curr = line.split("=")[0].strip()
    left=line.split("=")[1].strip().split(",")[0][1:]
    right=line.split("=")[1].strip().split(",")[1].strip()[:-1]
    d[curr]=(left,right)

steps=0
current="AAA"
while current != "ZZZ":
    if dirs[steps%len(dirs)] == "L":
        current = d[current][0]
    else:
        current = d[current][1]
    steps+=1
    

print(steps)
