#Sam Krimmel
#1/18/18
#how to use a loop

"""for i in range(1,101):
    if i%7 == 0 or '7' in str(i):
        print('Buzz')
    else:
        print(i)"""

i = 1
while i <= 100:
    if i%7 == 0 or '7' in str(i):
        print('Buzz')
    else:
        print(i)
    i = i+1