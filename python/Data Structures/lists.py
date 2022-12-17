'''
data structure is a collection of data elements (such as numbers or characters - or even other data structures)
that is structured in some way. the most basic data structure in Python is 'sequence'
- list is one of the sequence data structure
- lists are collection of items (strings, integers)
- lists are enclosed in []
- lists are index value and mutable[changeable] and each items are separated by comma.
'''

# List creation
list1 = [1,3,4,6]
print(list1)

#list length
print(len(list1))

#List append
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

#List insert
num = ['one']
num.insert(1, 'two') # here first insert argument is location and second is element
print(num)

num.remove('two')
print(num)

#list delete
items = ['one', 'two', 'three', 'four']
del items[1]
print(items)

# or we can use pop()
i = items.pop(2)
print(i)

#list related keyword in Python
thing = ['book', 'pen', 'paper']

if 'book' in thing:
    print('success')
    
if 'stone' not in thing:
    print('success')

#list reverse
thing.reverse()
print(thing)

'''
list sorting:
- easiest way to sort a list with sort()
- it takes a list and returns a new list with those elements in sorted order
- original list is not changed
'''

nums = [5,6,4,27,8,1]
sorted_nums = sorted(nums)
print('sorted list: ', sorted_nums)
print('original list: ', nums)

print('reverse sorted list: ', sorted(nums, reverse=True))

nums.sort()
print('sorted list: ', nums)

#string split to create a list
integer = 'one,two,three'
int1 = integer.split(',')
print(int1)

'''
list indexing:
- each item in the list has an assigned index value starting from 0
- accessing elements in a list is called indexing
'''
lst = [1,2,3,4,5]
print(lst[1])

#list slicing
numbers = [10,20,30,4]
#print all numbers
print(numbers[:])

#print from index 0 to 2
print(numbers[0:3])

# print alternate elements in a list
print(numbers[::2])

'''
list count
'''
numb = [1,2,4,2,5,1,3]
print(numb.count(1))

'''
list looping
'''
for n in thing:
    print(n)
    
#list comprehension

#without
squares = []
for row in range(10):
    squares.append(row**2)
print(squares)

#using list comprehension
squares = [row**2 for row in range(10)]
print(squares)

'''
nested list comprehension
'''
# suppose we have a matrix

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

# transpose of a matrix without list comprehension
transposed = [] # creating a transpose matrix of given matrix

for i in range(4): # going to each of the columns i.e 4 columns
    new_list = []
    for row in matrix:
        new_list.append(row[i]) # taking first elements from each row and putting in new_list i.e. 1,5,9
    transposed.append(new_list) # and append new_list to transposed list

print(transposed)