
''' 
- polymorphism means many forms.
- polymorphism includes two concepts: 1. Overloading 2. Overriding
- This method of Overloading, which includes same name function with a
  different argument in one class
- Method Overriding which includes same name, method in pattern, adolescent child class
  with same arguments.
'''

# Overloading 
class myClass:
    def fun(self):
        return 10
    def fun(self, num1, num2):
        return num1 + num2
    
obj1 = myClass()
print(obj1.fun(33, 67))

print('\n')

# Overriding
class parent:
    def fun(self, num1, num2):
        return num1 + num2

class child(parent):
    def fun(self, num1, num2):
        return num1 * num2

obj1 = child()
print(obj1.fun(10, 32))
obj2 = parent()
print(obj2.fun(10, 32))