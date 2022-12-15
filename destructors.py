'''
Destructors are called upon when a Python object needs to be cleaned up. 
It basically has a completely opposite role of a constructor and is used 
to reverse the operations that a constructor performs. Destructors are mainly 
deployed to organize in a program and to implement the standards for coding.

Python’s garbage collector automatically handles memory management. However, 
destructors do exist in Python, and this article explains their use and 
functioning.

We use the __del__() function as the destructor in Python. When the programmer 
calls the __del__() function, all the object references get removed, which is
known as garbage collection.

syntax:

def __del__(self):
    # Write destructor body here
    

The advantages of using destructor in Python programs are below.

1. Memory space is freed as unnecessary space-consuming objects are deleted automatically.
2. It is easy as it gets invoked automatically.
'''
class Fruits:
# Calling constructor
    def __init__(self):
        print('Fruits created.')
# Calling destructor
    def __del__(self):
        print('Destructor called, Fruits deleted.')
        
obj = Fruits()
del obj