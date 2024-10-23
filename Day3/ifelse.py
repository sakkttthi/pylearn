a = 5
b = 10

if a>b:
    print("greater") #indentation is important (white space)
elif a==b:
    print("equal")
else:
    print('No condition is true')

# Short hand if
if a <b: print('b is greater')

# Short hand if else
print('a is greater') if a>b else print('b is greater')

print('A') if a>b else print("=") if a==b else print('b')

# AND OR NOT    
if a>b and a==b:
    print('and condition')

if b<a or a==b:
    print('or condition')

if not a>b:
    print('not condition')


# Nested if 
age= 25

if age != 0:
    if age >= 18:
        print('Eligible to vote')
    else:
        print('Not eligible to vote')
else:
    print('Recheck age')

# PASS  - if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
if a>b:
    pass

