f = open("input.txt", mode="r")

def hash(string):
    cv = 0
    for letter in string:
        cv += ord(letter)
        cv *= 17
        cv = cv % 256
    return cv


box = [[] for i in range(256)]
for line in f:
    parts = line.strip().split(",")
    for part in parts:
        if "=" in part:
            label = part.split("=")[0]
            box_number = hash(label)
            alreadyin = -1
            for i in range(len(box[box_number])):
                if label in box[box_number][i]:
                    alreadyin = i
            if alreadyin == -1:
                box[box_number].append(part.replace("=", " "))
            elif alreadyin != -1:
                print(box[box_number][alreadyin])
                box[box_number][alreadyin] = box[box_number][alreadyin].replace(box[box_number][alreadyin].split(" ")[1],part.split("=")[1])
        elif "-" in part:
            label = part.split("-")[0]
            box_number = hash(label)
            alreadyin2 = -1
            for i in range(len(box[box_number])):
                if label in box[box_number][i]:
                    alreadyin2 = i
            if alreadyin2 != -1:
                del box[box_number][alreadyin2]
print(box)

total = 0
for i in range(len(box)):
    for j in range(len(box[i])):
        total += (i+1) * (j+1) * int(box[i][j].split(" ")[1])

print(total)




