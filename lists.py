'''
a list is a collection of similar or different types of data.
a list is created in python inside [], separated by commas
'''

fruits = ['strawberry', 'lemon', 'jackfruit']
print(fruits)

# accessing python list
print(fruits[0])

# -ve index in python
print(fruits[-2])

# slicing a list
print(fruits[0:])
print(fruits[0:1])
print(fruits[:])
print(fruits[0:-1])

# adding elements to list
num = [1,2,3,4]
num.append(9)
print(num)

# change list
languages = ['Python', 'Dart', 'C++']

# changing the third item to 'C'
languages[2] = 'C'

print(languages)  # ['Python', 'Dart', 'C']

# remove list
languages.remove('Dart')
print(languages)

# iterating list
for fruit in fruits:
    print(fruit)
    
# list's length
print(len(fruits))

# List Comprehension:
# consists of an expression followed by for statement inside [] brackets

numbers = [i*i for i in range(1,4)]
print(numbers)