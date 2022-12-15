'''
An object is simply a collection of data (variables) and methods (functions). 
Similarly, a class is a blueprint for that object.
'''
# creating class
class myClass:
    "Hello Python Developers.."
    a = 10
    def value(self):
        print("Value method executed successfully...")
        
# creating a class object
obj = myClass()

# calling method
obj.value()

# calling attributes
print(obj.__doc__)
print(obj.a)