# Tuple is Ordered, un - changable & accepts duplicate ()

mytuple = ('apple','banana','apple','cherry')
mystr = ('car')
print(mytuple)

print(len(mytuple))

print(type(mytuple)) #<class 'tuple'>
print(type(mystr)) #<class 'str'> creating tuple with one item is a String

newtuple = tuple(('apple','kalan','shroom')) #double bracket
print(newtuple)

# Access tuple 
print(mytuple[1])
print(mytuple[-1])
print(mytuple[1:3])

# Check 
if 'apple' in mytuple:
    print('apple is present' , mytuple.count('apple'))

# Updating tuple with a workaround 
edittuple = ("apple", "banana", "cherry")
y = list(edittuple) #convert to list and edit
y[0] = "mushroom"
y.append("orange")
edittuple = tuple(y)
print(edittuple)

# Adding two tuple 
z = ('mango','pineappple')
edittuple += z
print(edittuple)

# Deleting values 
ty = list(edittuple)
ty.remove("cherry")
edittuple = tuple(ty)
print(edittuple)

# Unpacking - extract the values back into variables
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list

cars = ('benz','bmw','honda','suzuki') #packing
(costly, *luzury, budget) = cars #unpacking

print(costly) #benz
print(luzury) #['bmw', 'honda']
print(budget) #suzuki

# Loop
for x in cars:
    print(x)

for y in range(len(cars)):
    print(cars[y])

z=0
while z < len(cars):
    print(cars[z])
    z = z+1

# Join 
newt = cars + edittuple
print(newt)

# Multiply 
mult = newt * 2
print(mult)
