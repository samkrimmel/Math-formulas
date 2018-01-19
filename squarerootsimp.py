#Sam Krimmel
#1/19/18
#squarerootsimp.py - simplifies the square root of a number

from math import sqrt

a = int(input('Simplify the square root of: '))
s = sqrt(1)
for x in range(a,1,-1):
    if a%x == 0 and sqrt(x).is_integer():
        s = x
print(sqrt(s),'square root',a/s)


