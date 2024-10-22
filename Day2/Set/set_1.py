# A set is a collection which is unordered(unindexed), unchangeable* (Once a set is created, you cannot change its items, but you can remove items and add new items.)
# no duplicates 
setdup = {'apple','banana','apple'}
print(setdup) #{'apple', 'banana'}

# The values True and 1 are considered the same value in sets, and are treated as duplicates
# The values False and 0 are considered the same value in sets, and are treated as duplicates
setdup1 = {'apple','banana','cherry',True,1,2}
print(setdup1) #{'banana', True, 2, 'cherry', 'apple'}

print(type(setdup1)) #<class 'set'>

newset = set (('apple','banana','cherry')) #double bracket
print(newset)

# Access - set is unindexed
for x in newset:
    print(x)

print ('banana' not in newset)

# Add
newset.add('kiwi')
print(newset)

#add from another set
tropical = {"pineapple", "mango", "papaya"}
newset.update(tropical)
print(newset)

mylist = ["car", "bike"] #adding any collection type: list is used for example here
newset.update(mylist)
print(newset)

# Remove
# If the item to remove does not exist, remove() will raise an error.
# If the item to remove does not exist, discard() will NOT raise an error.
# Sets are unordered, so when using the pop() method, you do not know which item that gets removed

fruity = {"apple", "banana", "cherry"}
fruity.remove('banana')
print(fruity)
fruity.discard('kiwi') #item not present in set
print(fruity)

print(newset)
x = newset.pop()
print(x)
print(newset)

newset.clear()
print(newset)

del newset

# Loop 
newset = {"apple", "banana", "cherry"}

for i in newset:
    print (i) # random order is printed
