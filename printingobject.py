'''
Python is an object-oriented language – because of this, much of everything 
in Python is an object. In order to create objects, we create classes, which 
are blueprints for objects. These classes define what attributes an object can
have and what methods an object can have, i.e., what it can do.

Let’s create a fairly simple Python class that we can use throughout 
this tutorial. We’ll create a Dog class, which will a few simple attributes 
and methods.
'''

class Dog:
    def __init__(self, name, age, puppies):
        self.name = name
        self.age = age
        self.puppies = puppies
        
    def birthday(self):
        self.age += 1
        
    def have_puppies(self, number_puppies):
        self.have_puppies += number_puppies
        
'''
What we’ve done here, is created our Dog class, which has the instance 
attributes of name, age, and puppies, and the methods of birthday() and 
have_puppies().

Let’s now create an instance of this object:
'''
teddy = Dog(name='Mario', age=3, puppies=0)

'''
We now have a Python object of the class Dog, assigned to the variable teddy. 
Let’s see how we can access some of its object attributes.
'''
#python objects:

print(teddy.name)

print(dir(teddy)) # python dir's to print object's attributes

print(vars(teddy)) # vars prints object's attributes

# vars prints same as print(teddy.__dict__)