'''
strings in python are immutable i.e. not changed
'''

message = 'Namaste'

# assign new string message variable
message = 'Nepal'
print(message)

# multi liner string
message = '''
Kathmandu is the capital city of Nepal.
'''
print(message)

# compare strings

a = 'Namaste'
b = 'World'

if (a == b):
    print('matched')
else:
    print('not matched')
    
# join strings

a = "Hello, "
b = "Wednesday!"

c = a + b

print(c)

# iterate through strings
name = "Wednesday"

for col in name:
    print(col)
    
# string length()
print(len(name))

# string membership testing
print('y' in 'wednesday')

# python string formatting:
# make it easy to print values and variables

name = 'wednesday'
age = 16
print(f'Her name is {name} and {age} of age.')