# number1
# number = float(input("float number = "))
# print("rounded number =", round(number, 2))

# number2
# number1 = float(input("Enter the first number: "))
# number2 = float(input("Enter the second number: "))
# number3 = float(input("Enter the third number: "))
# print("The largest number is:", max(number1, number2, number3))
# print("The smallest number is:", min(number1, number2, number3))

# number3
# kilometer = float(input("kilometr =  "))
# meter = kilometer * 1000
# centimeter = kilometer * 100000
# print(kilometer, "kilometer =", meter, "meter =", centimeter, "centimeter")

# number4
# dividend = int(input("dividend = "))
# divisor = int(input("non-zero divisor = "))
# quotient, remainder = divmod(dividend, divisor)
# print("quotient =", quotient, "\nremainder =", remainder)

# number5
# celsius = float(input("celsius = "))
# fahrenheit = celsius * 9/5 + 32
# print(celsius, "celsius =", fahrenheit, "fahrenheit")

# number6
# number = float(input("number = "))
# numstr = str(number)
# print("the last digit =", numstr[-1])

# number7
# number = int(input("number = "))
# result = ("even", "odd")
# print(number, "is", result[number % 2], "number")

# number8
# a = float(input("a = "))
# b = float(input("b = "))
# a, b = b, a
# print("a =", a)
# print("b =", b)

# string1
# str = str(input("string = "))
# print(str.title())

# string2
# str = str(input("string = "))
# withouta = str.replace('a', '')
# withoutA = withouta.replace('A', '')
# withouti = withoutA.replace('i', '')
# withoutI = withouti.replace('I', '')
# withoute = withoutI.replace('e', '')
# withoutE = withoute.replace('E', '')
# withouto = withoutE.replace('o', '')
# withoutO = withouto.replace('O', '')
# withoutu = withoutO.replace('u', '')
# withoutvowels = withoutu.replace('U', '')
# print(withoutvowels)

# string3
# str = str(input("string = "))
# print("reversed string =", str[::-1])

# string4
# str = str(input("string = "))
# print("underscores instead of spaces =", str.replace(" ", "_"))

# string5
# str = str(input("string = "))
# reversedstr = str.lower()[::-1]
# result = ("not palindrome", "palindrome")
# print('"', str, "\" is", result[str.lower() == reversedstr])

# string6
# str = str(input("string = "))
# print("'o' instead of all occurrences of 'a' =", str.replace("a", "o").replace("A", "o"))

# string7
# email = str(input('email = '))
# indexof_atsign = email.find('@')
# print('username =', email[:indexof_atsign])

# string8
# str = str(input('string = '))
# print('titled =', str.title())

# string9
# str = str(input('string = '))
# print('without the first and last characters', str[1:-1])

# string10
# string = str(input('string = '))
# word = str(input('word = '))
# result = ('not present', 'present')
# print('A word "', word, '" is', result[word.lower() in string.lower()], 'in "', string, '"')

# string11
# char = str(input('character = '))
# string = str(input('string = '))
# result = ('no position', f"the first position at {string.lower().find(char.lower()) + 1}")
# print('"', char, '" has', result[char.lower() in string.lower()], 'in "', string, '"')

# string12
# str = str(input('string = '))
# print('without the last 3 characters =', str[:-3])

# string13
# string = str(input('string = '))
# chars = str(input('characters = '))
# withoutchars = string.lower().replace(chars.lower(), '')
# print('charaters', chars, 'is repeated', (len(string) - len(withoutchars))/len(chars), 'times in "', string, '"')

# string14
# str = str(input('string = '))
# print(str.replace(' ', '\n'))

# string15
# str = str(input('string = '))
# print(str[::2].replace(' ', ''))

# string16
# str = str(input('string = '))
# print(f'Title: <{str.lower().capitalize()}>')

# string17
# str = str(input("string = "))
# print("reversed string =", str[::-1])

# string18
# str1 = str(input('string1 = '))
# str2 = str(input('string2 = '))
# if len(str1) > len(str2):
#     print(f'\'{str1}\' is {len(str1) - len(str2)} more than \'{str2}\' in length')
# elif len(str2) > len(str1):
#     print(f'\'{str2}\' is {len(str2) - len(str1)} more than \'{str1}\' in length')
# else:
#     print(f'\'{str1}\' is equal to \'{str2}\' in length')

# boolean1
# username = str(input('username = '))
# password = str(input('password = '))
# print(username != '' and password != '')

# boolean2
# x = float(input('x = '))
# y = float(input('y = '))
# print(x == y)

# boolean3
# number = int(input('number = '))
# print(number > 0 and (number % 2 == 0))

# boolean4
# x = float(input('x = '))
# y = float(input('y = '))
# z = float(input('z = '))
# print(x != y and y != z and z != x)

# boolean5
# x = str(input('str1 = '))
# y = str(input('str2 = '))
# print(len(x) == len(y))

# boolean6
# number = int(input('number = '))
# print(number % 15 == 0)

# boolean7
# x = float(input('x = '))
# y = float(input('y = '))
# print(x + y > 50)

# boolean8
# number = float(input('number = '))
# print(10 <= number and number <= 20)
