'''
a function is a block of code that performs a specific task
'''

def nepaliStyleGreet():
    print('Namaste')
    
nepaliStyleGreet()

# function with arguments
def add_num(num1, num2):
    sum = num1 + num2
    print('Total Sum :', sum)

add_num(3,4)

# function return type
def cube_num(num):
    result = num*num*num
    return result

cube = cube_num(2)

print('Cube of a number: ', cube)

# python library function
import math

square_root = math.sqrt(16)

print('Square roo of num: ', square_root)

# use of function:
# code reusable like;
# function definition
def get_square(num):
    return num * num

for i in [1,2,3]:
    # function call
    result = get_square(i)
    print('Square of',i, '=',result)