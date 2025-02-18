def is_prime(n):
    if n<=0:
        return('The number that you entered is not positive integer!')
    else:
        m=int(n**(1/2))
        for i in range(2,m+1):
            if n%i==0:
                return False
            else:
                continue
        return True
for p in range(1,210):
    if is_prime(p) and not is_prime((210-p)):
        print(p)