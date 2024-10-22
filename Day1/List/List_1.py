# List is Ordered, changable & accepts duplicate []

thisList = ['apple', 50, 101.25, "banana",'pipeapple']

print(thisList)

for i in thisList:
    print(i)

# Access list 
print(thisList[2])

# Range of list 
print(thisList[2:5])

# check item exists
if "apple" in thisList:
    print('Apple is present')

# Change value 
thisList[3] = "Volvo"
print(thisList)
'''
If you insert more items than you replace, the new items will be inserted where you specified
If you insert less items than you replace, the new items will be inserted where you specified
'''
thisList[1:3] = ['car']
print(thisList)

# Insert 
thisList.insert(3, 'Benz')
print(thisList)

thisList.append("Hero")
print(thisList)

secondList = ['tvs', 'apache']
thisList.extend(secondList) #not only list we can also add tuple dict set
print(thisList)

# Remove
thisList.remove("apple")
print(thisList)

thisList.pop(3)
print(thisList)

thisList.pop() # removes last item from list

del secondList
# print(secondList)

thisList.clear()
print(thisList)

# Loop
thisList = ['apple', 50, 101.25, "banana",'pipeapple']
for x in thisList:
    print(x)

for y in range(len(thisList)):
    print(thisList[y])

i = 0
while i < len(thisList):
    print(thisList[i])
    i = i+1

# List comprehension
# Syntax: newlist = [expression for item in iterable if condition == True]
fruit = ['banana', 'mango', 'papaya']
newlist = [x for x in fruit]
print(newlist)

nextlist = [x for x in fruit if 'b' in x]
print(nextlist)

numlist = [x for x in range(50) if x < 10] 
print(numlist)

upperlist = [x.upper() for x in fruit]
print(upperlist)

hellolist = ['hello' for x in fruit]
print(hellolist)