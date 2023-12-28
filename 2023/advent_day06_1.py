f = open("input.txt", "r")

t=f.readlines()
times=[int(i) for i in t[0].split(":")[1].strip().split(" ") if i!=""]
distances=[int(i) for i in t[1].split(":")[1].strip().split(" ") if i != ""]

total=1
for i in range(len(times)):
    ways=0
    race_time=times[i]
    race_record=distances[i]
    for j in range(race_time+1):
        if j*(race_time-j)>race_record:
            ways+=1
        
    total*= ways

print(total)
