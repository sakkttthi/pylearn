# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
fruit = ["apple",'mango','orange']
for x in fruit: print(x)

for y in 'apple':print(y) #string

for z in range  (10): # range is 0 to 9
    print(z) #prints 7
    if z == 7:
        break

for a in range(5):
    if a == 3:
        break
    print(a) #stops at 2

for b in fruit:
    if b == "mango":
        continue
    print(b)

for c in range(10):
    print(c)
else:                   #else block execute after loop is completed
    print('completed!')

for a in range(5):
    if a == 3:
        break #else wont be executed if we use a break in loop
    print(a) 
else:
    print('completed')

# Nested
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruit:
        print(x,y)

# Empty for loop 
for i in range(2):
    pass