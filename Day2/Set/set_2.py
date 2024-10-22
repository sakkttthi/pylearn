# Join Sets

# Union - The union() method allows you to join a set with other data types, like lists or tuples
# The  | operator only allows you to join sets with sets, and not with other data types (tuple,list) like you can with the  union() method.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3
print(myset)

