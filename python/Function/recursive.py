'''
Recursion:
In python, a function can call other functions. it is even possible for the function to call itself.
these type of function is called recursive functions.
'''

#to print factorial of a number using recursion

def factorial(num):
    return 1 if num == 1 else (num * factorial(num - 1))

num = 5
print("Factorial of {0} is {1} ".format(num, factorial(num)))

# to print a fibonacci sequence using recursive function
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2) # num if num <=1 is a boundary case like f(0) = 0, f(1) =0+1
#fibonacci(num-1) + fibonacci(n-2) is a recursive function

nterms = 10
print("Fibonacci sequence:")
for n in range(nterms):
    print(fibonacci(n))