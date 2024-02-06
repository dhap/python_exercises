prev = ""
romeString = "MCMXCIX"
numm = 0

for i in romeString[::-1]:
    inver = 1
    if i < prev:
        inver = inver * -1
    if i == "I":
        numm = numm + (1  * inver)
    elif i == "V":
        numm = numm + (5 * inver)
    elif i == "X":
        numm = numm + (10 * inver)
    elif i == "L":
        numm = numm + (50 * inver)
    elif i == "C":
        numm = numm + (100 * inver)
    elif i == "D":
        numm = numm + (500 * inver)
    elif i == "M":
        numm = numm + (1000 * inver)
    prev = i
print(numm)