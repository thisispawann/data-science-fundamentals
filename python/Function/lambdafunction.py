'''
in python, a lambda function is a special type of function without the function name like;
'''

greet = lambda : print('Hello World')
greet()

# lambda function with argument
# lambda that accepts one argument
greet_user = lambda name : print('Hey there,', name)

# lambda call
greet_user('Wednesday')


#square a number with lambda function

num = (3,4,5,9)
square = list(map(lambda x:x**2, num))
print(square)