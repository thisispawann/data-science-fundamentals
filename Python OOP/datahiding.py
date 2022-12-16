'''
Data Hiding: 
- it means hiding the internal details of an object.
- an object's attributes mau or may not be visible outside the class definition
- we need to name attributes with a double underscore prefix
and those attributes then are not be directly visible to outsiders
- Python protects those members by internally changing the name to 
include the class name
- we can access such attributes as by using the class name,
object._className__attrName
'''

class myClass:
    __var = 11
    def fun(self):
        self.__var += 2
        print(self.__var)

obj = myClass()
obj.fun()
print(obj.__var) # some data are hide so we could not see so error shown
#print(obj._myClass__var) # if we use this we receive expected result

'''
output: myClass object has no attribute __var that because inside of the function 
it is accessible and we can call the function but if we try to access it 
individually or privately, it is not possible
'''