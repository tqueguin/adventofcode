f = open("input.txt", mode="r")

points = {(0, 0)}
wallpoints = {(0, 0)}
x = 0
y = 0
max_x = 0
max_y = 0
min_x = 0
min_y = 0

for line in f:
    direction = line.split(" ")[0]
    number = int(line.split(" ")[1])
    if direction == "R":
        for i in range(number):
            x += 1
            if x > max_x:
                max_x = x
            points.add((x, y))
    if direction == "L":
        for i in range(number):
            x -= 1
            if x < min_x:
                min_x = x
            points.add((x, y))
    if direction == "D":
        for i in range(number):
            y += 1
            if y > max_y:
                max_y = y
            points.add((x, y))
            wallpoints.add((x, y))
    if direction == "U":
        for i in range(number):
            y -= 1
            if y < min_y:
                min_y = y
            points.add((x, y))
            wallpoints.add((x, y))

count = 0
for i in range(min_y-15, max_y+15):
    bc = 0
    for j in range(min_x-15, max_x+15):
        if (j,i) in wallpoints:
            bc += 1
            print(j,i)
        if (j,i) in points:
            count += 1

        else:
            if bc % 2 != 0:
                count += 1


print(count)
