# single level Inheritance
# parent/base class
class Animal:
    def speak(self):
        print("Animal is speaking!")
    
# child/derive class
class Dog(Animal):
    def bark(self):
        print("Dog is barking Now..")

# creating object and call 
d = Dog()
d.bark()
d.speak()

print('-----------------')
# Multi-level Inheritance
class A:
    def dA(self):
        print("A class method")

class B(A):
    def dB(self):
        print("B class method")
        
class C(B):
    def dC(self):
        print("C class method")


# now we have to create an object of 'C' class
c = C()
c.dA()
c.dB()
c.dC()

print('*******************')
# Multiple Inheritance
class A:
    def dA(self):
        print("A class method")

class B:
    def dB(self):
        print("B class method")
        
class C(A,B):
    def dC(self):
        print("C class method")


# now we have to create an object of 'C' class
c = C()
c.dA()
c.dB()
c.dC()

print('***************')
# Hierarchical Inheritance

class A:
    def dA(self):
        print("A class method")

class B(A):
    def dB(self):
        print("B class method")
        
class C(A):
    def dC(self):
        print("C class method")


# now we have to create an object of 'C' class
c = C()
c1 = B()
c.dA()
c.dC()
c1.dA()
c1.dB()