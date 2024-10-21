'''
Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators - related to bit values, seems bit complex

'''
a = 10
b = 5

# Arithmetic operators
print(a+b)

# Assignment operators
a += 3
print(a)

# Comparison operators
print(a == b)

# Logical operators
print(a>b and a>1)
print(a!=b or a == b)
print(not(a>b and a>1)) #Reverse the result

# Identity operators
# Comapre same object, with the same memory location
x = ['apple', 'banana']
y = ['apple', 'banana']
z= x

print(x is z) # x & z share same memory location too
print(x is y)
print(y is z)

# Membership operators  
fruit = ['apple', 'banana']
print('banana' in fruit)
print('banana' not in fruit)