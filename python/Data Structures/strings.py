'''
Strings:
- is a sequence of characters

'''

mystring = 'Hello'
print(mystring)

# accessing characters
print(mystring[1])

# iteration through string
count = 0
for row in "Namaste":
    if row == 'a':
        count += 1
print(count, ' letters found')

'''
string methods:
- lower(), upper(), join(), split(), find(), replace()
'''
print(mystring.lower())
print(mystring.upper())
print('-'.join(['Namaste', 'World']))

# replace
s1 = 'Dull Morning'

s2 = s1.replace('Dull', 'Good')
print(s1)
print(s2)

# Given string is Palindrome or not?

my_string = 'MadaM'

# convert to lower
my_string = my_string.lower()
#reverse string
reverse_string = reversed(my_string)

#check if the string is equal to reverse
if list(my_string) == list(reverse_string):
    print('word is palindrome')
else:
    print('not a palindrome')
    
# python program to sort words in alphabetic order:
my_string = "Today is a Friday"

#breakdown the string into list of words
words = my_string.split()

# sort the list
words.sort()

#print sorted words are
for word in words:
    print(word)