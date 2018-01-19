#Sam Krimmel
#1/19/18
#squarerootsimp.py - simplifies the square root of a number

from math import sqrt

a = int(input('Simplify the square root of: '))
y = 1
for x in range(1,a):
    if a%x == 0 and sqrt(x).is_integer():
        y = x
print(sqrt(y),'square root',a/y)


