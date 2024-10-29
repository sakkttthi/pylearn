'''The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.'''

try:
    print(x)
except NameError:                           #exception is related to variable
    print('Variable name isnt defines') 
except:                                     # can have multiple exept statments
    print('Something else went wrong')

# Else 
try:
    print('Hello')
except:
    print('Variable is wrong')
else:
    print('Nothing happened')
finally:
    print("Finally is executed regarless")

# Raise an exeption intentionally 
x = -1 
if x < 0:
    raise Exception('Numbers should be greater than 0')