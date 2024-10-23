# Join Sets

# Union - The union() method allows you to join a set with other data types, like lists or tuples
# The  (|) operator only allows you to join sets with sets, and not with other data types (tuple,list) like you can with the  union() method.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
list = ["apple", "bananas", "cherry"]
tuple = ("John", "Elena")
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset1 = set1 | set2 | set3
myset2 = set1.union(set2,set3) #union adds to set or new set
set1.update(list,tuple) # updates value of same set
print(myset1)
print(myset2)
print(set1)

# The intersection() method will return a new set, that only contains the items that are present in both sets (&) operator
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2) #Return a new set with elements common to the set and all others.
set4 = set1 & set2
print(set3)
print(set4)

set1.intersection_update(set2) #Update the set, keeping only elements found in it and all others.
print(set1)

# The values True and 1 are considered the same value. The same goes for False and 0.
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)
print(set3)

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set. (-) operator

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
set4 = set1- set2
print(set3)
print(set4)

set1.difference_update(set2)
print(set1)

# The symmetric_difference() method will keep only the elements that are NOT present in both sets. (^) operator
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
set4 = set1 ^ set2
print(set3)
print(set4)

set1.symmetric_difference_update(set2)
print(set1)