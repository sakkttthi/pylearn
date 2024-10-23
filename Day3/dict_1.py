# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

thisdict = {
    "Brand": "BMW",
    "Model": "320D",
    "Year": 2002,
    "Year": 2014, #donot allow duplicate
    "Color": ['red','blue','green'] #allows list
}

print(thisdict)
print(len(thisdict))
print(type(thisdict))

# Dict class 
newdict = dict(name= 'Ravi',work='CTO') #use equal to symbol
print(newdict)

# Accessing
print(newdict['name'])

x = newdict.get('work')
print(x)

y = newdict.keys()
print(y)

z = newdict.values()
print(z)

a = newdict.items() #returns pair is a set tuple
print(a)

# Check if exists 
if 'work' in newdict:
    print('Work of %s is %s' % (newdict['name'], newdict['work']))

#Change items
newdict['work'] = 'Programmer'
print(newdict)

newdict.update({'name':'Rajesh'})
print(newdict)

# Add items 
newdict["Experience"] = 5
print(newdict)

newdict.update({'location':'India'})
print(newdict)

# Remove item 
newdict.pop('location')
print(newdict)

newdict.popitem()
print(newdict) #removes last item, can also include keys to remove specific value pairs

del newdict ['work']
print(newdict)



newdict.clear() # clear all data
print(newdict)

del newdict # delete dict