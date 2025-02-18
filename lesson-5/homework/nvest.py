amount1=float(input('Enter the amount of the investment : '))
rate1=float(input('Enter an annual percentage rate : '))
years1=int(input('Enter a number of years : '))
def invest(amount, rate, years):
    for year in range(1,years+1):
        print(f'year {year}: ${round(amount*((1+rate)**(year)),2)}')
invest(amount=amount1, rate=rate1, years=years1)
