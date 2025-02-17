c=0
for i in range(2,100):
    n=int((i)**(1/2))
    for j in range(2,n+1):
        if i%j==0:
            c+=1
    if c==0:
        print(i)
    c=0
        

