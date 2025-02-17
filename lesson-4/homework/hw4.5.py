password=input('Enter a password ')
n=len(password)
if n<8:
    print('Password is too short.')
elif password==password.lower():
    print("Password is too short.")
else:
    print("Password is strong.")
