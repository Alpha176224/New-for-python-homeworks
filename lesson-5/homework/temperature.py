def convert_cel_to_far(C):
    F = C * 9/5 + 32
    return(round(F,2))
def convert_far_to_cel(F):
    C = (F - 32) * 5/9
    return(round(C,2))
Fahrenheit = float(input('Enter a temperature in degrees F: '))
print(f'{Fahrenheit} degrees F = {convert_far_to_cel(Fahrenheit)} degrees C')
Celsius=float(input('Enter a temperature in degrees : '))
print(f'{Celsius} degrees C = {convert_cel_to_far(Celsius)} degrees F')