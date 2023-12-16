f = open("input.txt", "r")

t=f.readlines()
times=[i for i in t[0].split(":")[1].strip().split(" ") if i!=""]
distances=[i for i in t[1].split(":")[1].strip().split(" ") if i != ""]
time=""
distance=""
for t in times:
    time+=t
for d in distances:
    distance+=d
time=int(time)
distance=int(distance)


ways=0
for j in range(time+1):
    if j*(time-j)>distance:
        ways+=1

print(ways)
