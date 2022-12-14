'''
a variable declared outside of the function or in global scope is called global variables.
this means that a global variable can be accessed inside or outside of the function.
'''

#declare global variable
message = 'Namaste'

def greet():
    #declare a local variable
    print('Local', message)
    
greet()
print('Global', message)

'''
this time we can access the message variable from outside of the greet() function.
this is because we have created the message variable as the global variable
'''