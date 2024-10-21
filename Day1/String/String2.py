a = "Hello, World"
print(a.upper())
print(a.lower())
print(a.split(","))
print(a.replace("World", "Python"))

b = " -Hello, Py- "
print(b.strip())

# Concat
x = 'Hello'
y = "World"
print(x+y)
print(x+" "+y)

# Format Strings
age = 36
txt = 'My name is John & age is '
# print (txt + age) #We cannot concat str and int

alttxt = f'My name is John & age is {age}' #include f
print(alttxt)

ntxt = f'This is a operation {50*20}'
print(ntxt)

# Escape char
t = "We are so called \"Vikings\" from the north"
print(t)

# String methods: https://www.w3schools.com/python/python_strings_methods.asp