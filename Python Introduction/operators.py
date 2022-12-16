'''
Arithmetic Operator
'''
a = 7
b = 2

# addition
print ('Sum: ', a + b)  

# subtraction
print ('Subtraction: ', a - b)   

# multiplication
print ('Multiplication: ', a * b)  

# division
print ('Division: ', a / b) 

# modulo
print ('Modulo: ', a % b)  

# a to the power b
print ('Power: ', a ** b)   

'''
Assignment Operator
'''
# assign 10 to a
a = 10

# assign 5 to b
b = 5 

# assign the sum of a and b to a
a += b      # a = a + b

print(a)

# Output: 15

#Comparison Operator
a = 5
b =2

print (a > b)    # True

# Logical Operator
a = 5
b = 6

print((a > 2) and (b >= 6))    # True

#Identity Operators
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)  # prints False

print(x2 is y2)  # prints True

print(x3 is y3)  # prints False