f = open("input.txt", "r")

total=0
for line in f:
    serie = [int(i) for i in line.strip().split(" ")]
    series = [serie]

    while serie.count(0) != len(serie):
        newserie = [serie[i+1]-serie[i] for i in range(len(serie)-1)]
        series.append(newserie)
        serie = newserie

    for i in range(len(series)-2, -1,-1 ):
        series[i].insert(0,series[i][0]-series[i+1][0])

    total += series[0][0]

print(total)