'''
Set:
- a set is an unordered collection of items. every element is unique (no duplicate)
- it doesn't support indexing
- set itself is mutable. we can add or remove items from it
- can be used to perform mathematical set operations like union, intersection, symmetric difference etc.
'''

#set creation
s = {1,2,3,4,5,6,7}
print(s)
print(type(s))

# set doesn't allow duplicate
s1 = {1,3,4,1,3}
print(s1)

# we can make set from list
s2 = set([1,2,3])
print(s2)

# add
s.add(8)
print(s)

# remove element
s.discard(8) 
print(s)

#pop() removes first element of a set
s.pop()
print(s)

# clear() tp remove all elements of set
s.clear()
print(s)

#Python Set Operations
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

#union of two sets using | operator
print(set1 | set2)

#another way of union
print(set1.union(set2))

#intersection
print(set1 & set2)

#set difference
print(set1 - set2)

'''
symmetric difference:
- set of elements in both set1 and set2 except those that are common in both.
'''
print(set1 ^ set2)

'''
Frozen set:
- it has characteristics of sets but we can't be changed once it's assign
- while tuple are immutable lists, frozen sets are immutable sets
- it can be created using function frozenset().
- sets being mutable are unhashable so they can't be used as dictionary keys. whereas, frozensets are hashable 
and can be used as keys to a dictionary.
- this datatype supports method like copy(), difference(), intersection(), issubset(),
symmetric_difference() and union().
- Being immutable it does not have method that add or remove elements
'''

set3 = frozenset([1,2,3,4])
set4 = frozenset([3,4,5,6])

#try to add element
#set3.add(5) # gives an error

print(set3 | set4)
print(set3 & set4)
print(set3 ^ set4)