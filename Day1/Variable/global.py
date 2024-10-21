
x = 'awsome' #Global variable

def myFun():
    x = 'Fantastic' #Local variable
    print('This year is ' + x)

myFun()

print('Today is ' + x)

# Using Global keyword

def firstfun():
    global name 
    name = "rajasekar"
    print('Name is ' + name)

firstfun()

print('Another name is ' + name) #Here we are accessing name which is created under a fucntion with global keyword