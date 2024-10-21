print('Hello World')

# Using quotes
print("It's alright")
print("He is called 'John'")
print('My name us "Victor"')

# assign string to valriable
a = 'car'
print(a)

# assign multiple string to valriable
b = """It's alright, 
He is called 'Ram', 
His name is 'john'"""
print(b)

c = '''It"s alright, He is called "Ram", His name is "john"'''
print(c)

# Strings are arrays
name = "Hello world"
print(name[1])
print(len(name))

# Looping through a string
for x in name:
    print(x)

# Check string 
txt = "This is a free world"
print("free" in txt)

if "free" in txt:
    print("Good lines by Amstrong")

print("Tree" not in txt)

if "Tree" not in txt:
    print("casata")

# Slicing
lake = "Hello, Python"
print(lake[2:5])
print(lake[2:]) #Slice till end
print(lake[:5]) #Slice from start
print(lake[-5:-2]) #Slice from last