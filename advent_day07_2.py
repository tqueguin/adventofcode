f = open("input.txt", mode="r")

cards=["A","K","Q","T","9","8","7","6","5","4","3","2","J"]
def strength(hand):
    d={}
    for card in hand:
        if card not in d:
            d[card]=1
        else:
            d[card]+=1


    if "J" in d and len(d)!=1:
        js=d["J"]
        del d["J"]
        sorted_d = sorted(d.items(), key=lambda x:x[1])
        d[sorted_d[-1][0]]+=js
        
    d=list(d.values())
    d.sort(reverse=True)
        
    if len(d)==1:
        return 7
    if len(d)==2 and d[0]==4:
        return 6
    if len(d)==2 and d[0]==3:
        return 5
    if len(d)==3 and d[0]==3:
        return 4
    if len(d)==3 and d[0]==2:
        return 3
    if len(d)==4 and d[0]==2:
        return 2
    if len(d)==5:
        return 1


def beats(hand1,hand2):
    if strength(hand1)>strength(hand2):
        return True
    if strength(hand2)>strength(hand1):
        return False
    for i in range(len(hand1)):
        if cards.index(hand1[i])<cards.index(hand2[i]):
            return True
        if cards.index(hand1[i])>cards.index(hand2[i]):
            return False

hands=[]
for l in f:
    hands.append([l.split(" ")[0],int(l.split(" ")[1])])

ordered_hands=[]
for hand in hands:
    index=0
    for i in range(len(ordered_hands)):
        if(beats(ordered_hands[i][0],hand[0])):
            index=i+1
    ordered_hands.insert(index,hand)

total=0
for i in range(len(ordered_hands)):
    total += (len(ordered_hands)-i)*ordered_hands[i][1]

print(total)
            
    
