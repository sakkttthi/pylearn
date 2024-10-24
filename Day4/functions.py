# A function is a block of code which only runs when it is called.

# Creating
def myfun():
    print('Hello function')

# Calling 
myfun()

# Arguments -1
def nameCon(fname):
    print('Name is %s' %(fname))

nameCon("Ravi")
nameCon('Raj')

# Arguments -2
def twoName(fname,lname):
    print(fname, lname)

twoName("emily","clark")

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly

def myKids(*kids):
    print("my last kid is %s" %(kids[1]))

myKids("apple","Sanjay","Surya")

# Keyword Arguments
# You can also send arguments with the key = value syntax.
def child1(child1,child2,child3):
    print("my last child is %s" %(child2))

child1(child1="sanjay",child2="Ram",child3="Lachu")

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly
def son(**son):
    print("My son is a " + son["profession"])
son(name = "Hari", profession='Engineer')

# Default Parameter Value
# If we call the function without argument, it uses the default value
def myCountry(country = 'India'):
    print('This is my ' + country)

myCountry('Sweden')
myCountry('Pak')
myCountry() #no parameter is passed

# Lists as argument

def list (food):
    for x in food:
        print(x)

fruit=['apple','mango','banana']

list(fruit)

# Return value 
def fiveTables (num):
    return 5 * num

print(fiveTables(5))

# Empty function 
def emptyFun():
    pass

# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments
def next(x, /):
    print(x)

# next(x=4) #TypeError: next() got some positional-only arguments passed as keyword arguments: 'x'

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments

def key(*,x):
    print(x)

# key(3) #TypeError: key() takes 0 positional arguments but 1 was given

# Combine Positional-Only and Keyword-Only
def combine (a,b,/,*,c,d):
    print(a,b,c,d)

combine(5,6,c=10,d=15)

#Recurssion - learn it 
