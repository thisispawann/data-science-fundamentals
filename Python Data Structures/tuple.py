'''
tuple:
- similar to lists
- tuple is immutable that is it can't be changed
'''

# tuple creation

t = (1,23,4)
print(t)

#nested tuple
t = (1, 'adam', 2, 'epochs')
print(t)

#only () is not enough
t = ('wednesday')
print(type(t))

#need a comma at the end
t = ('wednesday',)
print(type(t))

#accessing elements in tuple
t = ('a', 'b', 'c', 'd')
print(t[1])
print(t[-1])

#nested tuple
t = ('abc', ('bcd', 'def'))
print(t[1])

#slicing
print(t[:])
print(t[:1])
print(t[:-1])

# length 
print(len(t))

#sort
t = (3,5,2,5,1)
new_t = sorted(t)
print(new_t)

# largest element in a tuple
t = (2,3,41,24)
print(max(t))