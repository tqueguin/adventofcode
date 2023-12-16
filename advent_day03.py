f = open("input.txt", mode="r")
matrix=[]
i=0
for line in f:
    matrix.append([])
    for j in range(len(line)):
        matrix[i].append(line[j])
    i = i + 1

def touchesgear(amatrix,k,l):
    touches=False
    sx=k
    sy=l
    ex=k
    ey=l
    if k>0:
        sx=k-1
    if k<len(amatrix)-1:
        ex=k+1
    if l>0:
        sy=l-1
    if l<len(amatrix)-1:
        ey=l+1

    gearspos=[]
    for m in range(sx,ex+1):
        for n in range(sy,ey+1):
            if amatrix[m][n] == "*":
               gearspos.append(str(m)+str(n))
               

    return gearspos

gears={}
res=0
i=0
for i in range(len(matrix)):
    j=0
    number=""
    gearstouched=[]
    while(j<len(matrix[i])):
        if matrix[i][j] in "0123456789":
            number+=matrix[i][j]
            if len(touchesgear(matrix,i,j)) != 0:
                for truc in touchesgear(matrix,i,j):
                    if truc not in gearstouched:
                        gearstouched.append(truc)
        else:
            if number != "" and len(gearstouched) != 0:
                for geartouched in gearstouched:
                    if geartouched not in gears:
                        gears[geartouched]=[0,1]
                    gears[geartouched]=[(gears[geartouched][0]+1),(gears[geartouched][1]*int(number))]
            number=""
            gearstouched=[]
        j = j + 1
    if number != "" and len(gearstouched) != 0:
                for geartouched in gearstouched:
                    if geartouched not in gears:
                        gears[geartouched]=0
                    gears[geartouched]=[gears[geartouched][0]+1,gears[geartouched]*int(number)]

for gear in gears:
    if gears[gear][0]==2:
        res = res + gears[gear][1]
print(res)
print(gears)


