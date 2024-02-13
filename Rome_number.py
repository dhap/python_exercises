"""
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
"""

s = "MCMXCIV"
summa = 0
A = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

for i, j in enumerate(s[:-1]):
    if A.get(j) >= A.get(s[i+1]):
        summa += A.get(j)
    else:
        summa -= A.get(j)
summa += A.get(s[-1])
print(summa)
