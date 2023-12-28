f = open("input.txt", mode="r")

def hash(string):
    cv = 0
    for letter in string:
        cv += ord(letter)
        cv *= 17
        cv = cv % 256
    return cv

total = 0
for line in f:
    parts = line.strip().split(",")
    for part in parts:
        total += hash(part)
print(total)
