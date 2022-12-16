# import standard math module

import math
print('the value of pi is: ', math.pi)

# import module by renaming it

import math as m

print(m.pi)

# python from..import statement
# we can import specific names from a module without importing the module as a whole

from math import pi

print(pi)

# import all names
from math import *

print('the value of pi is: ', pi)

from calculate import *

a = 10

b = 8

result = mul(a, b)
print(result)

import datetime
print(datetime.datetime.now())