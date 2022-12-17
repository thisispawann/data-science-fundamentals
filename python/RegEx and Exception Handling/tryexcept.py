'''
The try except statement can handle exceptions. Exceptions may happen when you
run a program.
'''

a = 10
b = 0

try:
  c = a / b
  print(c)
  
except ZeroDivisionError as e:
  print("You cannot divide a number by zero")