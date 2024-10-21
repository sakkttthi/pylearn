import random

x = 1
y = 2.2
z = 8j

print(type(x)) #int
print(type(y)) #float
print(type(z)) #complex (Number & j)

# Conversion
x = float(y)
y = complex(x)
z = int(5.33)

print(x) 
print(y) 
print(z) 

print(type(x)) 
print(type(y)) 
print(type(z)) 

# random number
print(random.randrange(1,500))
