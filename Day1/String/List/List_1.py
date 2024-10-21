# List is Ordered, Not changable & accepts duplicate

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