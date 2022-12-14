# generally in python array infers to the lists.
# we'll focus on a module named array. array module allows us to 
# store a collection of numeric values.

''' 
to create an array of numeric values, we need to import the array module. 
'''
import array as arr
a= arr.array('i', [1,2,3]) # array() has at least one unicode character. so, hee 'i'. otherwise it becomes list

print('First element: ', a[0])
print('First element: ', a[-1])