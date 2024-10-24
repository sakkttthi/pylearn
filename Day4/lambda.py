# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax - lambda arguments : expression

x = lambda a: a+10
print(x(10))

y = lambda fname: 'First name is %s' %(fname)
print(y('Hari'))