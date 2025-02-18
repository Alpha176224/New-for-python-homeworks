n=int(input('Enter a positive integer: '))
factors=(f'{factor} is a factor of {n}' for factor in range(1,n+1) if n%factor==0)
for i in factors:
    print(i)