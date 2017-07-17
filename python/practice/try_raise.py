import math
a = int(input('Enter a number:'))
try:
    print(math.sqrt(a))
except:
    print('Bad value for square root')
    print('Using absolute value instead')
    print(math.sqrt(abs(a)));

# or you can use raise to define an error message
if a < 0:
    raise RuntimeError('You can\'t use a negative number!')
else:
    print(math.sqrt(a))
