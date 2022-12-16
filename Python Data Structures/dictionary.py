'''
Dictionary:
- is an unordered collection of items that means can't have index
- key, value pairs
'''
# dict creation
my_dict = {
    'name' : 'pawan',
    'age' : 20
}
print(my_dict)

# dict access
print(my_dict['name'])
print(my_dict.get('age'))

# add or modify elements
my_dict['age'] = 25
my_dict['degree'] = 'B.Tech'
print(my_dict)

# dict delete or remove element
print(my_dict.pop('age'))
print(my_dict)

#printing keys
print(my_dict.keys())

# get all dictionary methods
d = {}
print(dir(d))