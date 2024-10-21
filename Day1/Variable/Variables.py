x = 3
y = 'Hari'

print(x)
print(y)

# Knowing the type of variable
print (type(x)) #<class 'int'>
print (type(y)) #<class 'str'>

# Casting
a = str(3)
b = int(3)
c =float(3)
print(a,b,c) #3 3 3.0

# String accepts both single & double quotes
name1 = 'Hari'
name3 = "Raj"
print(name1,name3)

# Variable names are case-sensitive
Fname = "Shankar"
fname = "Rajini"
print(Fname,fname)

# Assiging multiple values
fruit1, fruit2, fruit3 = 'apple', 54, "John doe"
print(fruit1,fruit2,fruit3)

# assigning same values to multiple variable
car1 = car2 = car3 = "Volvo"
print(car1,car2,car3)

# unpack collection
orange = ['apple', 'pine', 'bike']
f,g,h = orange
print(f,g,h) 

# Output variable
print (f+g+h) #using + (using + in printing a int & str throws error)
print(f,g,h) #using ,