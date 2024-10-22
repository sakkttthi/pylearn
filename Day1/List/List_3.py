thislist = ["orange", "Mango", "kiwi", "pineapple", "Banana"]

# Sorting - by default sort fucntion is case sensitive (Capital first)
thislist.sort()
print(thislist)

# To reverse list in desc order 
thislist.sort(reverse=True)
print(thislist)

# We can sort using key value pairs
thislist.sort(key=str.lower)
print(thislist)

# To reverse the list irrespective of alphanumeric 
thislist.reverse()
print(thislist)

# Copy list1 = list2 wont copy the list, it will still have reference (any change made in kist1 will reflect on list2)
copylist = thislist.copy()
print("This is a copy list " , copylist)

copylist1 = list(thislist)
print(copylist1)

copylist2 = thislist[:]
print(copylist2)

# Join list 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

for x in list2:
    list1.append(x)
print(list1)

list1.extend(list3)
print(list1)

print(list1.count('a'))
