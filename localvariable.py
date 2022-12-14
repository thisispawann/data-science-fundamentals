'''
when we declare variables inside a function, these variables will have a local scope (within the function)
we cannot access them outside the function. these type of variables are called local variables
'''

def greet():
    #local variable
    message = 'Hello'
    
    print('Local', message)
    
greet()

# when it try variable outside the function
print(message)

# so, the variable only be accessed within a function