'''
loops are used to repeat a block of code
- for loop
- while loop
'''

'''
for loop:
for loop is used to run a block of code for a certain number of times.
it is used to iterate over any sequence such as list, tuple, string, etc.
'''

countries = ['Nepal', 'Korea', 'Japan', 'Russia']

for c in countries:
    print(c)
    
'''
loop with range():
a range is a series of values between two numeric intervals.
we use range() to define a range of values
'''
for c in range(3):
    print(c)


# while loop
# while loop is used to run a specific code until a certain condition is met.

i = 1
while i <=10:
    print(i)
    i += 1
    
# while loop to display game level
current_level = 0
final_level = 5

game_completed = True

while current_level <= final_level:
    if game_completed: 
        print('You have passed level', current_level)
        current_level += 1

print('Level Ends')