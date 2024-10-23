# Loop 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
    print(x) #prints key

for y in thisdict:
    print(thisdict[y]) #prints value

for z in thisdict.keys():
    print(z)

for a in thisdict.values():
    print(a)

for b in thisdict.items(): # print pairs
    print(b)

# Copy 
copyd = thisdict.copy()
print(copyd)

copy1 = dict(thisdict)
print(copy1)

# Nested dict 

school = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# or 

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# Accessing 
print(myfamily["child1"]["name"])

