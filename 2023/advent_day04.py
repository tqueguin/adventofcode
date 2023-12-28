f = open("input.txt", mode="r")
total=0
parcourus=set()

def numberCardsWon(dico,indice):
    parcourus.add(indice)
    if indice not in dico:
        return 1
    else:
        som=0
        for truc in dico[indice]:
            som+=numberCardsWon(dico,truc)
        return som+1
    


d={}
notind=0
i=1
for line in f:
    wins = line.split("|")[0].split(":")[1].strip().split(" ")
    wins2 = [i for i in wins if i != ""]
    wins=wins2
    nums = line.split("|")[1].strip().split(" ")
    wins = set(wins)
    nums = set(nums)

    good=0
    for num in nums:
        if num in wins:
            good+=1
    if good>0:
        d[i]=[j for j in range(i+1,i+1+good)]
    i+=1



for caca in range(1,i):
    total+=numberCardsWon(d,caca)
print(total)
