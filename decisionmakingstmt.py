'''
There are some situations when we need to make a decision and decide what to do next. 
We deal with these types of situations with the decision making statements in Python.
Decision-making statements present in Python are:-

if statement
if..else statements
nested if statements
if-elif ladder

'''

# if statement
age = 19
if(age>=18):
    print('eligible to vote')
    

# if..else statements
a = 10
if (a == 7):
    print('code is inside if block')
else:
    print('code is inside else block')
    

# nested if statements
a = 10;
b = 20;

if(a==10):
    if(b==20):
        print('executed')
    else:
        print('throw exception')
else:
    print('hell yeah')
    

# if-elif statement
a = 3
if (a == 2):
    print('Code inside if block')
elif (a == 3):
    print('Code inside elif block')
else:
    print('Code inside else block')