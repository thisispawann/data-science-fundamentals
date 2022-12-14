'''
A set is an unordered collection of items. Every set element is unique (no duplicates) and 
must be immutable (cannot be changed).
A set is created by placing all the items (elements) inside curly braces {}, separated by comma, 
or by using the built-in set() function
'''
thing = {'rock', 'book'}
print(thing)
print(type(thing))

thing.add('hat')
# thing.update('stone')
print(thing)

# iterating through a set
for fruit in set('jack'):
    print(fruit)
    
# python frozenset
'''
Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. 
While tuples are immutable lists, frozenset are immutable sets.
Sets being mutable are unhashable, so they can't be used as dictionary keys. 
On the other hand, frozenset are hashable and can be used as keys to a dictionary.
Frozenset can be created using the frozenset() function.
'''
#set:
fruits = {"Apple", "Banana", "Cherry", "Apple", "Kiwi"}

print('Unique elements:', fruits)

# Add new fruit
fruits.add("Orange")
print('After adding new element:', fruits)

# Size of the set
print('Size of the set:', len(fruits))

#frozenset:
fruits = {"Apple", "Banana", "Cherry", "Apple", "Kiwi"}
basket = frozenset(fruits)

print('Unique elements:', basket)

# Add new fruit throws an error!
basket.add("Orange")
print('After adding new element:', basket)