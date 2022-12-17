'''
A Regular Expression (RegEx) is a sequence of characters that defines a search pattern.

Python has a module named re to work with RegEx.
for instance:
^a...s$
The above code defines a RegEx pattern. The pattern is: any five letter string starting with a and ending with s.
'''
import re

pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	



# python regex

# 1. re.findall()


# Program to extract numbers from a string

import re

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)


#2 re.split()
import re

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string) 
print(result)

#3 re.search()
'''
The re.search() method takes two arguments: a pattern and a string. 
The method looks for the first location where the RegEx pattern produces 
a match with the string. If the search is successful, re.search() returns 
a match object; if not, it returns None.

syntax:
match = re.search(pattern, str)
'''


import re

string = "Python is fun"

# check if 'Python' is at the beginning
match = re.search('\APython', string)

if match:
  print("pattern found inside the string")
else:
  print("pattern not found")  

# Output: pattern found inside the string

#4 re.match()
import re
str = "\\tHello Python Programming"
obj1 = re.match("\\thello", str, re.I) #no match

str = "\tHello Python Programming"
ob1 = re.match("\\thello", str, re.I) #\thello is matching