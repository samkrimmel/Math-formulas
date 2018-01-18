#Sam Krimmel
#1/17/18
#lineequation - finds the equation of a line from two given points

x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))


print('y=mx+b')
if (x2-x1) == 0:
    print('Vertical line, not a function')
elif (y2-y1) == 0:
    print('Horizontal line at y =',y1)
else :
    m = ((y2-y1)/(x2-x1))
    print('m = ',m,'and b = ',(y1-(x1*m)))

