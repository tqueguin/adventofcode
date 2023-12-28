f = open("input.txt", mode="r")
sum=0
for line in f:
    id=int(line.split(":")[0].split(" ")[1])
    games=line.split(":")[1].split(";")

    maxs={}
    maxs["red"]=0
    maxs["green"]=0
    maxs["blue"]=0
    for game in games:
        balls=[]
        for subgame in game.split(","):
            balls.append(subgame.strip())
        for ball in balls:
            color=ball.split(" ")[1]
            number=ball.split(" ")[0]
            number=(int)(number)
            if(number > maxs[color]):
                maxs[color]=number
    sum = sum + (maxs["red"]*maxs["green"]*maxs["blue"])
print(sum)
    
