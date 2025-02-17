import random
s='yes'
while s in ['Y', 'YES', 'y', 'yes', 'ok']:
    n=random.randint(1,100)
    a=0
    for i in range(10):
        m=int(input('? = '))
        if i==9 and m!=n:
            s=input("You lost. Want to play again? ")
            break
        elif n<m:
            print('Too high!')
        elif n>m:
            print('Too low!')
        else:
            s=input("You guessed it right! Want to play again? ")
            break
        
