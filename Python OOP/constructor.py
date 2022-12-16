# example 1
class app:
    def __init__(self, name): # __init__ initialize constructor of particular class
        print("Hello", name)

a = app("joe")

print("------------------------")

# example 2
class Student:
    # constructor 
    def __init__(self, name, age):
        self.name = name
        self.age  = age
        print("His name is " f'{self.name}' " and he is " f'{self.age}' " years old.")
    # class method
    def myMethod(self, num):
        print("The cube of number is: ", num**3)
        
std = Student("Joe", 20)
std.myMethod(4)

