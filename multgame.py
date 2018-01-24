#Sam Krimmel
#1/24/18
#multgame.py - gives the user up to 10x10 multiplication problems and stops when they've answered five correctly

from random import randint

ques = 0


while ques < 6:
    num1 = randint(1,10)
    num2 = randint(1,10)
    print('What is:', str(num1),'x', str(num2))
    ans = int(input('= '))
    if ans == (num1*num2):
        print('Correct!')
        ques = ques+1
    else:
        print('Nope')
