'''
Abstraction classes in Python:
- An abstract class can be useful when we are designing large functions.
- An abstract class is also helpful to provide the standard interface
  for different implementations of components.
- Python provides the 'abc' module to use the abstraction in Python program.

Syntax:
from abc import ABC
class ClassName(ABC):
    
we import the ABC class form the abc module.
'''
from abc import ABC, abstractmethod
class Car(ABC):
    def mileage(self):
        pass
class Tesla(Car):
    def mileage(self):
        print('The mileage is 30 kmph')
class Suzuki(Car):
    def mileage(self):
        print('The mileage is 25 kmph')

t = Tesla()
t.mileage()
s = Suzuki()
s.mileage()
